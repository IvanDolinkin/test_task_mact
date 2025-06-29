from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, validates
from sqlalchemy import  Column, Integer, String, Date, Time

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "app.db"

engine = create_engine(f"sqlite:///{DB_PATH}")
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date)
    time = Column(Time)
    click_count = Column(Integer)

    @validates('name')
    def validate_name(self, key, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        return name


    def __repr__(self):
        return f"ItemDB({self.id=}, {self.name=}, {self.date=}, {self.time=}, {self.click_count=})"

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
