from sqlalchemy import Column, DATETIME, Integer, Float, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Bithumb(Base):
    __tablename__ = 'bithumb'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DATETIME)
    price = Column(Float)
    volume = Column(Float)
    currency = Column(VARCHAR(5))

    def __init__(self, date, price, volume, currency):
        self.date = date
        self.price = price
        self.volume = volume
        self.currency = currency

    def __repr__(self):
        return "Bithumb('%s', '%s', '%s', '%s')".format(self.date, self.price, self.volume, self.currency)


class Korbit(Base):
    __tablename__ = 'korbit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DATETIME)
    price = Column(Float)
    volume = Column(Float)
    currency = Column(VARCHAR(5))

    def __init__(self, date, price, volume, currency):
        self.date = date
        self.price = price
        self.volume = volume
        self.currency = currency

    def __repr__(self):
        return "Korbit('%s', '%s', '%s', '%s')".format(self.date, self.price, self.volume, self.currency)


class Coinone(Base):
    __tablename__ = 'coinone'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DATETIME)
    price = Column(Float)
    volume = Column(Float)
    currency = Column(VARCHAR(5))

    def __init__(self, date, price, volume, currency):
        self.date = date
        self.price = price
        self.volume = volume
        self.currency = currency

    def __repr__(self):
        return "Coinone('%s', '%s', '%s', '%s')".format(self.date, self.price, self.volume, self.currency)
