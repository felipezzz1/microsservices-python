from fastapi import FastAPI

import uvicorn
from mylib.logic import wiki as wiki_logic
from mylib.logic import search_wiki
from mylib.logic import phrase as phrase_logic

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki or /phrase"}

@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"search" : result}

@app.get("/wiki/{value}")
async def wiki(value: str):
    """Retrieve wikipedia page"""

    result = wiki_logic(value)
    return {"wiki" : result}

@app.get("/phrase/{value}")
async def phrase(value: str):
    """Retrieve wikipedia page and return phrases"""

    result = phrase_logic(value)
    return {"phrase" : result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
