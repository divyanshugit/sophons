import re
import os

import json
from dotenv import load_dotenv
from sophons.utils.models import OpenAIModel

load_dotenv()


def json_formatter(text):
    long_summary_regex = r"\*\*Long Summary:\*\*(.*?)(?=\*\*Short Summary:\*\*)"
    short_summary_regex = r"\*\*Short Summary:\*\*(.*?)(?=\*\*Categories:\*\*)"
    categories_regex = r"\*\*Categories:\*\*\s*(.*)"

    # Extracting the sections
    long_summary = re.search(long_summary_regex, text, re.DOTALL).group(1).strip()
    short_summary = re.search(short_summary_regex, text, re.DOTALL).group(1).strip()
    categories = (
        re.search(categories_regex, text, re.DOTALL).group(1).strip().split("\n")
    )

    # Removing numbers from categories
    categories = [category.split(". ", 1)[1] for category in categories]

    # Creating the final dictionary
    result = {
        "long_summary": long_summary,
        "short_summary": short_summary,
        "categories": categories,
    }

    result = json.dumps(result, indent=4)
    return result
