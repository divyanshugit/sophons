from llama_index.readers.web import SimpleWebPageReader

def get_blog(url):
  documents = SimpleWebPageReader(html_to_text=True).load_data([url])
  return documents[0].text
