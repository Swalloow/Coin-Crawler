from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import Config


class Database:
    def __init__(self):
        self.engine = create_engine(Config.DATABASE_URI, convert_unicode=False, echo=True)
        self.session = Session(bind=self.engine)

    def query(self, query):
        self.session.query(query)
        self.session.commit()

    def insert(self, model):
        self.session.add(model)
        self.session.commit()

    def __del__(self):
        self.session.close()
        self.engine.dispose()
