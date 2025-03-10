
from langchain_community.vectorstores import FAISS
from app.config.config import endpoint
from app.config.model_config import embeddings, llm
from app.utils.context import format_docs
from app.models.model import json_schema
from app.prompt.template import RAG_PROMPT
def rag(query):
    loaded_faiss = FAISS.load_local(endpoint, embeddings, allow_dangerous_deserialization=True)
    relevant_docs = loaded_faiss.similarity_search(query,k=3)
    context  = format_docs(relevant_docs)
    structured_llm = llm.with_structured_output(json_schema)
    response = structured_llm.invoke(RAG_PROMPT.format(context=context,question=query))
    return response