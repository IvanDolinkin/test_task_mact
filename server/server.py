from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field
from sqlalchemy import func
from datetime import date as date_type, time as time_type, datetime
from server.database import Session, ItemDB


app = FastAPI()


class ItemAdd(BaseModel):
    name: str
    click_count: int = Field(default=0, exclude=True)


class Item(ItemAdd):
    id: int
    date: date_type
    time: time_type
    click_count: int


class ItemID(BaseModel):
    status: str
    added_id: int


class ItemsPaginated(BaseModel):
    items: List[Item]
    total: int
    page: int


@app.post(path="/item", response_model=ItemID)
def add_item(item: ItemAdd):
    with Session() as session:
        item_db = ItemDB(
            name=item.name,
            date=datetime.now().date(),
            time=datetime.now().time(),
            click_count=item.click_count
        )
        session.add(item_db)
        session.commit()
        return {"status": "OK", "added_id": item_db.id}


@app.get(path="/items", response_model=ItemsPaginated)
def get_all_items(
        page: int = 1,
        num_records: int = 5
):
    offset = (page - 1) * num_records
    with Session() as session:
        items = session.query(ItemDB).order_by(ItemDB.id).offset(offset).limit(num_records).all()
        total = session.query(func.count(ItemDB.id)).scalar()
    return {
        "items": items,
        "total": total,
        "page": page
    }


@app.get(path="/")
def get_root():
    return {"go to": "http://127.0.0.1:8000/docs"}
