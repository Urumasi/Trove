from datetime import datetime, timedelta
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime

from ..database import db
from ..mixins import CRUDModel


class drop(CRUDModel):
    __tablename__ = 'drop'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    flux = Column(Integer, nullable=False, index=False)
    eye = Column(Integer, nullable=False, index=False)
    chest = Column(Integer, nullable=False, index=False)
    cache = Column(Integer, nullable=False, index=False)
    twice = Column(Integer, nullable=False, index=False)
    thrice = Column(Integer, nullable=False, index=False)
    quad = Column(Integer, nullable=False, index=False)
    penta = Column(Integer, nullable=False, index=False)
    comment = Column(String, nullable=False, index=False)
    def __init__(self, **kwargs):
        self.datum_vlozeni = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

class cenyd(CRUDModel):
    __tablename__ = 'cenyd'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    eye = Column(Integer, nullable=False, index=False)
    chest = Column(Integer, nullable=False, index=False)
    cache = Column(Integer, nullable=False, index=False)
    twice = Column(Integer, nullable=False, index=False)
    thrice = Column(Integer, nullable=False, index=False)
    quad = Column(Integer, nullable=False, index=False)
    penta = Column(Integer, nullable=False, index=False)
    def __init__(self, **kwargs):
        self.datum_vlozeni = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

class den(CRUDModel):
    __tablename__ = 'den'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    flux = Column(Integer, nullable=False, index=False)
    eye = Column(Integer, nullable=False, index=False)
    chest = Column(Integer, nullable=False, index=False)
    cache = Column(Integer, nullable=False, index=False)
    twice = Column(Integer, nullable=False, index=False)
    thrice = Column(Integer, nullable=False, index=False)
    quad = Column(Integer, nullable=False, index=False)
    penta = Column(Integer, nullable=False, index=False)
    comment = Column(String, nullable=False, index=False)
    def __init__(self, **kwargs):
        self.datum_vlozeni = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)