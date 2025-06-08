from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
                         )

#Case 1
# docs = loader.load()
# print(type(docs),len(docs))  # List : Every loader return a python list of documents objects
# print(type(docs[0]))   # Document object : Each element in list is Langchain document object with two major attributes
# print(docs[476].page_content)
# print(docs[0].page_content)                       # 1. page_content 2. metadata




# Case 2
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)