from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os


class RAGIndexes:    
    
    
    def __init__(self, pdf_list,k=5,search_type="similarity"):
        
        self.pdf_list = pdf_list
        self.all_documents = []
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"  # You can change this to any HuggingFace model
        )
        self.vectorstore = Chroma(
            embedding_function=self.embeddings,
            persist_directory='test_chroma_db',
            collection_name='test_vector_db' # Directory to store the vectorstore

        )
        
        
        self.k = k
        self.search_type = search_type 
        self.search_kwargs = {"k":self.k}      


    def load_documents(self):
        
        for pdf in self.pdf_list:
            try:
                self.loader = PyMuPDFLoader(pdf)
            except Exception as e:
                print(f"Error loading {pdf}: {e}")
                continue
            documents = self.loader.load()
            self.all_documents.extend(documents)
            print(f"Loaded {len(documents)} documents from {pdf}")
        print(f"Loaded {len(self.all_documents)} documents from {self.pdf_list}")
        
    def split_documents(self):
        self.split_docs = self.text_splitter.split_documents(self.all_documents)
        print(f"Split into {len(self.split_docs)} chunks")
    
    def create_vectorstore(self):
        self.vectorstore.add_documents(documents=self.split_docs)
        print("Documents added to vectorstore successfully")
    
    
    def create_retriever(self,score_threshold=0.8,lambda_mult =0.5):
        
        if self.search_type == "similarity_score_threshold":
            self.search_kwargs["score_threshold"] = score_threshold
        
        elif self.search_type =="mmr":
            self.search_kwargs ["lambda_mult"] = lambda_mult
        
        self.retriever = self.vectorstore.as_retriever(
        search_type=self.search_type,
        search_kwargs=self.search_kwargs
    )
    
    
    def build_indexes(self):
        self.load_documents()
        self.split_documents()
        self.create_vectorstore()
        self.create_retriever()
        print("RAG Indexes created completed successfully")
        return self.retriever
    
    def query(self,query_text):
        return self.retriever.invoke(query_text)
        
    
    def query_with_score(self,query_text):
        return self.vectorstore.similarity_search_with_score(query_text,k=self.k)
    
    


def get_retreiver(pdf_list,k):
    rag_obj = RAGIndexes(pdf_list,k)
    rag_obj.build_indexes()
    return rag_obj

if __name__ == "__main__":
    k = 2 # Number of documents to retrieve
    # Example PDF list
    pdf_list = ['https://cs229.stanford.edu/notes2022fall/decision-trees.pdf',
                 '/Users/shoeb/Desktop/jupyterNotebook/Generative_AI/LLM/RAG/data/docs/cs229_lectures/MachineLearning-Lecture01.pdf']
    
    rag_retreiver = get_retreiver(pdf_list,k)
    
    
    # Example usage of the retriever
    
    query_text = "What is Decison Tree?"
    results = rag_retreiver.query(query_text = "What is Decison Tree?")

    print(f"Found {len(results)} relevant documents for query: '{query_text}'")
    
    for doc in results:
        print(doc.page_content)  # Print first 200 characters of each document






