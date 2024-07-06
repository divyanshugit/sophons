from langchain_community.document_loaders import WebBaseLoader

def get_blog(url):
  loader = WebBaseLoader(url)
  documents = loader.load()

  return documents