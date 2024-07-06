import time
from typing import List, Dict
import os
import urllib3

from together import Together
from sophons.utils.logger import logger


class TogetherAPIModel:
    API_TIMEOUT = 100
    API_MAX_RETRY = 3
    API_RETRY_SLEEP = 5

    def __init__(self, model_name, api_key):
        self.model_name = model_name
        self.api_key = api_key
        self.client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

    def generate(self, prompt: str):
        # system_prompt = {
        #     "role": "system",
        #     "content": "You are a helpful assistant. You reply with concise and day to day used language.",
        # }

        # chat_tempalate = [system_prompt]

        # print(prompt)
        # print(chat_tempalate)
        # message = chat_tempalate.append({"role": "user", "content": prompt})
        # print(message)
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=prompt,
        )
        return response.choices[0].message.content


class GroqAPIModel:
    API_TIMEOUT = 100
    API_MAX_RETRY = 3
    API_RETRY_SLEEP = 5

    def __init__(self, model_name, url, api_key):
        self.model_name = model_name
        self.url = url
        self.api_key = api_key

    def generate(self, prompt: List[Dict]):
        for _ in range(self.API_MAX_RETRY):
            try:
                logger.info(f"Generating response for {prompt}")
                headers = {
                    "Authorization": f"Bearer {self.api_key}",  # Replace with your actual API key
                    "Content-Type": "application/json",
                }
                data = {
                    "messages": prompt,  # [{"role": "user", "content": prompt}],
                    "model": self.model_name,
                }
                resp = urllib3.request(
                    "POST",
                    self.url,
                    headers=headers,
                    timeout=urllib3.Timeout(self.API_TIMEOUT),
                    json=data,
                )
                resp_json = resp.json()

                output = resp_json["choices"][0]["message"]["content"]
                break
            except:
                logger.warning(f"Error with {prompt} in  response: {resp_json}")
                time.sleep(self.API_RETRY_SLEEP)
        return output
