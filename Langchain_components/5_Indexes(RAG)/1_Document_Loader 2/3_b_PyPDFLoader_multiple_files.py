from langchain_community.document_loaders import PyPDFLoader




class RAGIndexes:

    def __init__(self,pdf_list):
        self.pdf_list = pdf_list
        
    
    def load_documents(self):
        self.documents =[]
        
        for pdf in self.pdf_list:
            self.loaders = PyPDFLoader(pdf)
            documents = self.loaders.load()
            self.documents.extend(documents)

        print(f"Loaded {len(self.documents)} documents from {len(self.pdf_list)} files")
        return self.documents


    def run(self):
        self.load_documents()
        print("RAG Indexes created successfully")
        return self.documents


if __name__ == "__main__":
    pdf_list = [
        'https://cs229.stanford.edu/notes2022fall/decision-trees.pdf',
        '/Users/shoeb/Desktop/jupyterNotebook/Generative_AI/LLM/RAG/data/docs/cs229_lectures/MachineLearning-Lecture01.pdf'
    ]
    rag_indexes = RAGIndexes(pdf_list).run()
    