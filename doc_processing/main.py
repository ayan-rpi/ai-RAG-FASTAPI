from langchain_community.document_loaders import PyPDFLoader

file_path = "./thebook.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = FAISS.from_documents(documents=splits, embedding=OpenAIEmbeddings(model="text-embedding-3-small"))
vectorstore.save_local("knowledge_base")