from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0
)

# Case 1 : Using text
text ="""My name is Shoeb
I am 34 years old


I live in Gurgaon
How are you?"""

result = splitter.split_text(text)
print(result)  # List of chunks

# Case 2 : Using documents
loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()
result = splitter.split_documents(docs)  # results is list of document object with page_content, metadata

print(type(result), len(docs), type(result[0]))
print(result[10].page_content)   #  page_content is a chunk of original text