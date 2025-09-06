from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# Path parameters with types
"""
Endpoint to retrieve an item by its ID.

Args:
    item_id (int): The unique identifier of the item to be retrieved.

Returns:
    dict: A dictionary containing the item ID.
"""
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

"""
    Query Parameters
Endpoint to retrieve items with optional query parameters.
Args:
    q (str, optional): An optional query string to filter items.
    limit (int, optional): The maximum number of items to return. Default is 10.
Returns:
    dict: A dictionary containing the query parameters.
"""
@app.get("/items/")
async def read_items(q: str = None, limit: int = 10):
    return {"q": q, "limit": limit}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
