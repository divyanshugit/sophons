import os
from dotenv import load_dotenv
from openai import OpenAI
from sophons.utils.models import GroqAPIModel, TogetherAPIModel
from sophons.utils.logger import logger

load_dotenv()

model = TogetherAPIModel(
    model_name="mistralai/Mixtral-8x22B-Instruct-v0.1",
    api_key=os.environ.get("TOGETHER_API_KEY"),
)
system_prompt = {
    "role": "system",
    "content": "You are a helpful assistant. You reply with concise and day to day used language.",
}

chat_tempalate = [system_prompt]


def get_long_summary(blog_text):
    user_message = (
        """You will generate increasingly concise, entity-dense summaries of the above Article.
                Repeat the following 2 steps 2 times.
                Step 1. Identify 1-3 informative Entities (";" delimited) from the Article which are missing from the previously generated summary.
                Step 2. Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the Missing Entities.
                A Missing Entity is:
                - Relevant: to the main story.
                - Specific: descriptive yet concise (5 words or fewer).
                - Novel: not in the previous summary.
                - Faithful: present in the Article.
                - Anywhere: located anywhere in the Article.
                Guidelines:
                - The first summary should be long (8-10 sentences, ~350 words) yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this article discusses") to reach -80 words.
                - Make every word count: re-write the previous summary to improve flow and make space for additional entities.
                - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
                - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
                - Missing entities can appear anywhere in the new summary.
                - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.
                Remember, use the exact same number of words for each summary.
                Answer in JSON. The JSON should be a list (length 5) of dictionaries whose keys are
                "Missing_Entities" and "Denser_Summary", the blog content is given below:\n."""
        + blog_text
    )
    logger.info("Generating long summary...")
    chat_tempalate.append({"role": "user", "content": user_message})
    summarized_text = model.generate(chat_tempalate)
    logger.info(f"Long Summary:\n {summarized_text}")
    final_text = ""
    while len(final_text) == 0:
        try:
            final_text = str(eval(summarized_text)[-1]["Denser_Summary"])
            return final_text
        except:
            summarized_text = model.generate(chat_tempalate)

def get_long_summary_video(blog_text):
    user_message1 = (
        """Generate a 100 word summary of the content given below by including all important details."""
        + blog_text
    )
    user_message2 = (
        """From the content given below, generate a document of key take-aways of the content. 'Key Take-aways' should be header 1. All the take-aways should be under it as Header 2 and They should all be explained in around 100 words each.
            For example:
            **KEY TAKE-AWAYS**

            insert Key Take-away 1
            Explain in 100 words.

            insert Key Take-away 2
            Explain in 100 words.

            insert Key Take-away 3
            Explain in 100 words.

            insert Key Take-away 4
            Explain in 100 words.

            insert Key Take-away 5
            Explain in 100 words.

            insert Key Take-away 6
            Explain in 100 words.

            **CONCLUSION**
            Give a 200 word conclusion.
            """
        + blog_text
    )
    logger.info("Generating long summary...")
    chat_tempalate.append({"role": "user", "content": user_message1})
    summarized_text = model.generate(chat_tempalate)
    chat_tempalate.append({"role": "user", "content": user_message2})
    summarized_text += "\n\n"+model.generate(chat_tempalate)
    logger.info(f"Long Summary:\n {summarized_text}")
    return summarized_text


def get_short_summary(blog_text):
    user_message = (
        """You will generate increasingly concise, entity-dense summaries of the above Article.
                Repeat the following 2 steps 3 times.
                Step 1. Identify 1-3 informative Entities (";" delimited) from the Article which are missing from the previously generated summary.
                Step 2. Write a new, denser summary of one 15 words length which covers every entity from the previous summary plus the Missing Entities.
                A Missing Entity is:
                - Relevant: to the main story.
                - Specific: descriptive yet concise (2 words or fewer).
                - Novel: not in the previous summary.
                - Faithful: present in the Article.
                - Anywhere: located anywhere in the Article.
                Guidelines:
                - The first summary should be long (2 sentences, ~30 words) yet highly non-specific, containing little information beyond the entities marked as missing.
                - Make every word count: re-write the previous summary to improve flow and make space for additional entities.
                - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
                - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
                - Missing entities can appear anywhere in the new summary.
                - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.
                Remember, use the exact same number of words for each summary.
                Answer in JSON. The JSON should be a list (length 5) of dictionaries whose keys are
                "Missing_Entities" and "Denser_Summary", the blog content is given below:\n."""
        + blog_text
    )
    logger.info("Generating single line summary...")
    chat_tempalate.append({"role": "user", "content": user_message})
    summarized_text = model.generate(chat_tempalate)
    logger.info(f"Short Summary:\n {summarized_text}")
    final_text = ""
    while len(final_text) == 0:
        try:
            final_text = str(eval(summarized_text)[-1]["Denser_Summary"])
            return final_text
        except:
            summarized_text = model.generate(chat_tempalate)


def get_summary(blog_text):
    logger.info("Getting summary...")
    long_summary = get_long_summary(blog_text)
    short_summary = get_short_summary(blog_text)
    return {"long_summary": long_summary, "short_summary": short_summary}

def get_summary_video(blog_text, length):
    logger.info("Getting summary...")
    if length<1200:
        long_summary = get_long_summary(blog_text)
    else:
        long_summary = get_long_summary_video(blog_text)
    short_summary = get_short_summary(blog_text)
    return {"long_summary": long_summary, "short_summary": short_summary} 

