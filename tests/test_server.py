from datetime import time, date
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.database import Base, ItemDB

engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)

@pytest.fixture(autouse=True)
def init_db():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


def test_add_item():
    with Session() as session:
        item_db = ItemDB(
            name="test_item",
            date=date(2025, 6, 29),
            time=time(18, 30),
            click_count=1
        )
        session.add(item_db)
        session.commit()

        assert item_db.id > 0
        assert item_db.name == "test_item"
        assert item_db.date == date(2025, 6, 29)


def test_fail_add():
    with Session() as session:
        with pytest.raises(ValueError, match="Name cannot be empty"):
            item_db = ItemDB(
                name="",
                date=date(2025, 6, 29),
                time=time(18, 30),
                click_count=1
            )
            session.add(item_db)
            session.commit()


def test_read_items():
    with Session() as session:
        test_item = ItemDB(
            name="item_to_read",
            click_count=10
        )
        session.add(test_item)
        session.commit()
        item_id = test_item.id

    with Session() as session:
        item = session.get(ItemDB, item_id)

        assert item is not None
        assert item.name == "item_to_read"
        assert item.click_count == 10
