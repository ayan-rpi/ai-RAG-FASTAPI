from pydantic import BaseModel

json_schema = {
    "title": "OutputSchema",
    "description": "Structure of the output",
    "type": "object",
    "properties": {
        "answer": {
            "type": "string",
            "description": "The answer of the question",
        },
    },
    "required": ["answer"]
}
class Query(BaseModel):
    """
    Input model for the API.  Requires a 'query' string.
    """
    query: str
