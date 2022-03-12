from typing import Tuple
from fastapi import Depends, FastAPI, Query

app = FastAPI()


async def pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)

@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

class Pagination:
    def __init__(self, maximum_limit: int = 100) -> None:
        self.maximum_limit = maximum_limit
    
    async def __call__(self, skip
    : int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> Tuple[int, int]:
        capped_limit = min(self.maximum_limit, limit)
        return (skip, capped_limit)

pag = Pagination(maximum_limit=50)
async def list(p: Tuple[int, int] = Depends(pag)):
    skip, limit = p
    return {"skip": skip, "limit": limit}