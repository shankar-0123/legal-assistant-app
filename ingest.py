from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders.csv_loader import CSVLoader

vectordb_file_path = "faiss_index"
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")


loader = CSVLoader(file_path='Indianconstitution.csv',encoding='utf-8-sig')
data = loader.load()


vectordb = FAISS.from_documents(documents=data,
                                    embedding=instructor_embeddings)


vectordb.save_local(vectordb_file_path)
    