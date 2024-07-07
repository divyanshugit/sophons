import json
import uuid
import re
from sophons.utils.video_extractor import get_transcript
from sophons.summarizer import (
    get_long_summary_video,
    get_long_summary,
    get_short_summary,
    get_categories,
)
from sophons.utils.update_db import add_row
from sophons.utils.update_vdb import update_vdb
from datetime import datetime, timezone
from llama_index.llms.openai import OpenAI
from sophons.utils.logger import logger
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent

import os
from dotenv import load_dotenv

from sophons.slack_reader import get_latest_message, get_channel_id
from sophons.utils.formatter import json_formatter

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")


channel_id = get_channel_id("content-dump")
logger.info(f"Getting the latest message from the channel: {channel_id}")
url, timestamp = get_latest_message(channel_id=channel_id)
logger.info(f"Extracting the transcript from the video: {url}")
title, thumbnail, transcript, duration = get_transcript(url)

youtube_regex = re.compile(
    r"^(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})(?:[&?=\w]*)$"
)
match = youtube_regex.match(url)

logger.info(f"Initalizing the agent summarizer...")

if match:
    long_summary_tool = FunctionTool.from_defaults(get_long_summary_video)
    short_summary_tool = FunctionTool.from_defaults(get_short_summary)
    category_tool = FunctionTool.from_defaults(get_categories)
else:
    long_summary_tool = FunctionTool.from_defaults(get_long_summary)
    short_summary_tool = FunctionTool.from_defaults(get_short_summary)
    category_tool = FunctionTool.from_defaults(get_categories)

llm = OpenAI(model="gpt-4o", temperature=0)

agent = ReActAgent.from_tools(
    [long_summary_tool, short_summary_tool, category_tool], llm=llm, verbose=True
)


response = agent.chat(
    f"Get the long summary, short summary and categories of the given text {transcript}."
)
print("**" * 20)
print(type(response))
print("Response from the agent:")
print(response)
print("**" * 20)
# print(response.__dict__)
response = response.response

json_response = eval(json_formatter(response))
print(type(json_response))

topic = json_response["categories"]
single_line_summary = json_response["short_summary"]
full_summary = json_response["long_summary"]

# summary = get_summary(transcript)
logger.info(f"Updating the data to VectorDB for topic: {topic}")
_ = update_vdb(transcript, topic)
posted_at = datetime.fromtimestamp(float(timestamp), tz=timezone.utc).isoformat()

# Print the result
logger.info(f"Adding the row to the database...")
_, _ = add_row(
    posted_at=posted_at,
    single_line_summary=single_line_summary,
    full_summary=full_summary,
    topic_name=topic,
    url=url,
    title=title,
)
with open("summary.json", "w") as f:
    json.dump(json_response, f, indent=4)
