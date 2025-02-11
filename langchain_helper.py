from langchain.vectorstores import FAISS
from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os

from dotenv import load_dotenv
load_dotenv() 

llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)

instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "faiss_index"

def get_qa_chain():
    
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings)

    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """You are a legal assistant chatbot, your name is "Nyaay Sahaayak", your main aim is to answer the queries related to the Indian laws and legal system,
    if the question is not related to Indian laws and legal system kindly say dont know about the given question
    Given the following context and a question, generate an answer based on the context or related to the Indian laws and legal system. The context given may not be always right
    for the given question, hence cross verify yourself inorder to give an accurate answer that is only related to Indian laws and legal system.
    Add some creativity to make the answer look readable and easily understandable. If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer,
    if the question is out of the Indian laws and legal system, strictly deny them that you are not trained for it and only here for Indian law and legal system.

    CONTEXT: {context}

    QUESTION: {question}
    
    """

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain

if __name__ == "__main__":
    chain = get_qa_chain()