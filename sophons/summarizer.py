import os
from openai import OpenAI
os.environ['OPENAI_API_KEY']=""
client=OpenAI()

def summarizer_long(blog_text):
    user_message="""You will generate increasingly concise, entity-dense summaries of the above Article.
                Repeat the following 2 steps 5 times.
                Step 1. Identify 1-3 informative Entities (";" delimited) from the Article which are missing from the previously generated summary.
                Step 2. Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the Missing Entities.
                A Missing Entity is:
                - Relevant: to the main story.
                - Specific: descriptive yet concise (5 words or fewer).
                - Novel: not in the previous summary.
                - Faithful: present in the Article.
                - Anywhere: located anywhere in the Article.
                Guidelines:
                - The first summary should be long (4-5 sentences, -100 words) yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this article discusses") to reach -80 words.
                - Make every word count: re-write the previous summary to improve flow and make space for additional entities.
                - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
                - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
                - Missing entities can appear anywhere in the new summary.
                - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.
                Remember, use the exact same number of words for each summary.
                Answer in JSON. The JSON should be a list (length 5) of dictionaries whose keys are
                "Missing_Entities" and "Denser_Summary", the blog content is given below:\n."""+blog_text
    summarized_text = client.chat.completions.create(model="gpt-4",messages=[{"role": "user", "content":user_message}]).choices[0].message.content
    final_text=""
    while(len(final_text)==0):
        try:
            final_text=str(eval(summarized_text)[-1]["Denser_Summary"])
            print("---GENERATED 100 WORDS LENGTH SUMMARY---")
            return final_text
        except:
            summarized_text = client.chat.completions.create(model="gpt-4",messages=[{"role": "user", "content":user_message}]).choices[0].message.content

def summarizer_line(blog_text):
    user_message="""You will generate increasingly concise, entity-dense summaries of the above Article.
                Repeat the following 2 steps 10 times.
                Step 1. Identify 1-3 informative Entities (";" delimited) from the Article which are missing from the previously generated summary.
                Step 2. Write a new, denser summary of one line length which covers every entity from the previous summary plus the Missing Entities.
                A Missing Entity is:
                - Relevant: to the main story.
                - Specific: descriptive yet concise (2 words or fewer).
                - Novel: not in the previous summary.
                - Faithful: present in the Article.
                - Anywhere: located anywhere in the Article.
                Guidelines:
                - The first summary should be long (2 sentences, -30 words) yet highly non-specific, containing little information beyond the entities marked as missing.
                - Make every word count: re-write the previous summary to improve flow and make space for additional entities.
                - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
                - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
                - Missing entities can appear anywhere in the new summary.
                - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.
                Remember, use the exact same number of words for each summary.
                Answer in JSON. The JSON should be a list (length 5) of dictionaries whose keys are
                "Missing_Entities" and "Denser_Summary", the blog content is given below:\n."""+blog_text
    summarized_text = client.chat.completions.create(model="gpt-4",messages=[{"role": "user", "content":user_message}]).choices[0].message.content
    final_text=""
    while(len(final_text)==0):
        try:
            final_text=str(eval(summarized_text)[-1]["Denser_Summary"])
            print("---GENERATED LINE LENGTH SUMMARY---")
            return final_text
        except:
            summarized_text = client.chat.completions.create(model="gpt-4",messages=[{"role": "user", "content":user_message}]).choices[0].message.content

def summary(blog_text):
    long_summary=summarizer_long(blog_text)
    line_summary=summarizer_line(blog_text)
    final_summary=[long_summary,line_summary]
    return final_summary