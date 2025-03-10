import sys
from pathlib import Path
import json

sys.path.append(str(Path(__file__).resolve().parent.parent))
from app.models.model import Query
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException

from app.chains.rag_chain import rag

app = FastAPI(title="RAG on Machine Learning")

@app.post("/query")
async def query_rag(query_data: Query):
    
    try:
        answer = rag(query_data.query)
        return json.loads(answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)