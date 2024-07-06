from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import re
import base64
import requests


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")
client = OpenAI()

def create_graph(graph):
    path = 'graph.png'
    graphbytes = graph.encode("utf8")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")

    url = "https://mermaid.ink/img/" + base64_string

    response = requests.get(url)

    with open(path, 'wb') as f:
        f.write(response.content)
    print(f"Graph image saved at {path}")

def get_graph(transcript):
  system_prompt = """Give the mermaid code to create a flowchart to summarize the given content effectively. The flowchart should be concise and be easily understandable in one look while also conveying all important information. The maximum depth should be 3 and should be in top-down configuration. You have to only include the key points of the content without unecessary details. Output only a json according to the given sample format. There should be no other text in the ouput other than the json.

                      Sanple Output:
                      {
                        "code" : "mermaid code here"
                      }
                      """
  completion = client.chat.completions.create(
                model='gpt-4o',
                messages=[{"role": "system", "content": system_prompt},
                            {"role": "user", "content": transcript}]
                )
  
  pattern = r'\{(.*?)\}'  
  match = re.search(pattern, completion.choices[0].message.content, re.DOTALL)

  try:
    print('retrying...')
    mm_code = json.loads(str('{'+match.group(1)+'}'))['code']
    create_graph(mm_code)
  except:
    get_graph(transcript)


