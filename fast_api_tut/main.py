from fastapi import FastAPI, Query,Body,Cookie,Header
from  pydantic import BaseModel


app = FastAPI()

@app.get("/")  # passing path parameters
async def read_root():
    return {"Hello": "World"}


items_db =[
    {"item_id": 1, "name": "item1"},
    {"item_id": 2, "name": "item2"},
    {"item_id": 3, "name": "item3"},
]

@app.get("/items")
async def get_items(skip: int = 0, limit: int = 10):
    return items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str | None= None, short: bool = False):

    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})    

    return item



class NewItem(BaseModel):
    name: str
    description: str | None
    price: float
    tax: float | None = None

@app.post("/items")
async def create_item(item: NewItem):    
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get("/users")
async def get_users(q: str | None = Query(None, min_length=3, max_length=10),important: int = Body(...)):
    result = {"q": q}
    if important:
        result.update({"important": important})
    return result
# it will return  using Body(...)
# {
#     "q": "test",
#     "important": 5
# }
# or else it will return if Body is not used 
# {
#     "q": "test",
#     "important": {
#        important:5
#      }
# }

@app.get("/cookies_tut")
async def get_item(cookie_id: str  = Cookie(None),accept_en: str = Header(None)):
    return {"cookie_id": cookie_id}