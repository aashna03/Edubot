# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.llms import CTransformers
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationalRetrievalChain
import sys
import os
print(os.path.exists("data/final_all_with_loc.csv"))
# from some_embedding_module import embeddings  
# DATA_PATH = 'data/'
DB_FAISS_PATH = 'vectorstore/db_faiss'

# Create vector database
def create_vector_db():
    loader = CSVLoader(file_path="data/final_all_with_loc.csv", encoding="utf-8", csv_args={'delimiter': ','})
    #loader = CSVLoader(file_path="E:/chatcsvAll/data/final_all_with_loc_new.csv", encoding="utf-8", csv_args={'delimiter': ','})
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                   chunk_overlap=20)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    # db = FAISS.from_documents(texts, embeddings, allow_dangerous_deserialization=True)
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    create_vector_db()
  

