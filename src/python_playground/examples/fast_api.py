from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

async def get_burgers(number: int) -> list[dict]:
    burgers = []
    for i in range(number):
        burgers.append({"name": f"burger {i}", "price": 10.0, "is_offer": True})
    return burgers

@app.get("/burgers")
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers

if __name__ == "__main__":
    # Swagger UI: http://localhost:8000/docs
    # ReDoc: http://localhost:8000/redoc
    uvicorn.run(app, host="0.0.0.0", port=8000)
