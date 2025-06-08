from langchain_community.document_loaders import TextLoader


loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()

print(type(docs),len(docs))  # List : Every loader return a python list of documents objects

print(type(docs[0]))   # Document object : Each element in list is Langchain document object with two major attributes
print(docs[0])
# print(docs[0].page_content)                       # 1. page_content 2. metadata


# print(docs[0].metadata)
# https://python.langchain.com/docs/integrations/document_loaders/