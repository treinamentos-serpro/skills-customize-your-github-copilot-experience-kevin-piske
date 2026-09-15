from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Inventory API")


class Item(BaseModel):
    id: int
    name: str
    description: str = ""
    price: float
    in_stock: bool = True


items = [
    Item(id=1, name="Keyboard", description="Mechanical keyboard", price=89.99, in_stock=True),
    Item(id=2, name="Mouse", description="Wireless mouse", price=49.50, in_stock=True),
]


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Inventory API!"}


# TODO: add GET /items
# TODO: add GET /items/{item_id}
# TODO: add POST /items
# TODO: add PUT /items/{item_id}
