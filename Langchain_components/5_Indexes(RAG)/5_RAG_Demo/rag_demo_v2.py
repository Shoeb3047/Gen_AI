from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


from langchain_community.vectorstores import Chroma
import os


class RAGDemo:

    def __init__(self, pdf_path_list):
        self.pdf_path_list = pdf_path_list
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = None
        self.documents = []

    def load_documents(self):
        for pdf_path in self.pdf_path_list:
            if pdf_path.startswith("http"):
                loader = PyPDFLoader(pdf_path)
            elif os.path.exists(pdf_path):
                loader = PyPDFLoader(pdf_path)
            else:
                raise FileNotFoundError(f"PDF file not found or URL invalid: {pdf_path}")

            docs = loader.load()
            self.documents.extend(docs)
            print(f"Loaded {len(docs)} documents from {pdf_path}")

    def split_documents(self):
        self.split_docs = self.text_splitter.split_documents(self.documents)
        print(f"Split into {len(self.split_docs)} chunks")

    def create_vectorstore(self):
        self.vectorstore = Chroma.from_documents(
            documents=self.split_docs,
            embedding=self.embeddings,
            persist_directory="test_pdf_vectorstore"
        )
        print("Vectorstore created with embeddings")

    def create_retriever(self):
        if self.vectorstore is None:
            raise ValueError("Vectorstore not created. Call create_vectorstore() first.")
        self.retriever = self.vectorstore.as_retriever()
        print("Retriever created from vectorstore")

    def run(self):
        self.load_documents()
        self.split_documents()
        self.create_vectorstore()
        self.create_retriever()
        print("RAG Indexes created successfully")
        return self.retriever

    def get_relevant_documents(self, query):
        if not hasattr(self, 'retriever'):
            raise ValueError("Retriever not created. Call run() first.")
        results = self.retriever.get_relevant_documents(query)
        return results


if __name__ == "__main__":
    pdf_list = [
        'https://cs229.stanford.edu/notes2022fall/decision-trees.pdf',
        '/Users/shoeb/Desktop/jupyterNotebook/Generative_AI/LLM/RAG/data/docs/cs229_lectures/MachineLearning-Lecture01.pdf'
    ]
    rag_demo = RAGDemo(pdf_list)
    retriever = rag_demo.run()

    query = "What is a decision tree?"
    results = retriever.invoke(query)

    print(f"Found {len(results)} relevant documents for query: '{query}'")
    for doc in results:
        print(doc.page_content[:200])  # Print preview
