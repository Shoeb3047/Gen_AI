from langchain_community.document_loaders import CSVLoader
from dotenv import load_dotenv
load_dotenv()

loader = CSVLoader(file_path="Social_Network_Ads.csv")

docs = loader.load()
print(type(docs), len(docs))  # List : Every loader return a python list of documents objects
print(docs[0].page_content)                       # 1. page_content 2. metadata


