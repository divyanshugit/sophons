from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import os
import json
import re
import cv2
import pytube as pt
import urllib.request
import urllib
from sophons.utils.language_codes import language_codes
from sophons.utils.logger import logger

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")
client = OpenAI()


def get_keyframes(transcript):
    system_prompt = """Given the transcript of a video, you have to identify and output the 5 most important timestamps in the video which would help in summarizing the video. You need to use chain of thought reason to determine the important timestamps. Output only a json according to the given sample format. There should be no other text in the ouput other than the json.
                      Sample Format:

                      {
                          "chain_of_thought_for_each_frame": ["reason1","reason2","reason3","reason4","reason5"]
                          "keyframe_timestamps": [1, 2, 3, 4, 5]
                      }
                      """
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript},
        ],
    )

    pattern = r"\{(.*?)\}"
    match = re.search(pattern, completion.choices[0].message.content, re.DOTALL)

    try:
        keyframes = json.loads(str("{" + match.group(1) + "}"))["keyframe_timestamps"]
    except:
        return get_keyframes(transcript)
    return keyframes


def extract_frames_from_video(timestamps, output_folder="keyframes"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture("temp.mp4")

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    frame_paths = []
    for timestamp in timestamps:
        frame_number = int(timestamp * fps)

        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        ret, frame = cap.read()

        if ret:
            frame_filename = os.path.join(output_folder, f"frame_{timestamp:.2f}.png")
            cv2.imwrite(frame_filename, frame)
            frame_paths.append(frame_filename)
        else:
            print(f"Warning: Could not retrieve frame at {timestamp} seconds.")

    cap.release()

    return frame_paths


def get_transcript(video_url, language="English"):
    try:
        lang_id = language_codes[language]
    except Exception as e:
        logger.error(f"We don't have support for {language}: {e}")

    logger.info(f"Getting transcript for video: {video_url}")
    video_id = video_url.split("=")[1]
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_id}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    logger.info(f"Getting video metadata for video...")
    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        title = data["title"]
        thumbnail = data["thumbnail_url"]
    logger.info(f"Extracting transcript for video: {title}...")
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang_id])
    text = " ".join([t["text"] for t in transcript])
    return title, thumbnail, text
