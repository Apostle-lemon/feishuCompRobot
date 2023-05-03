from sqlalchemy import Column, DateTime, Index, String, TIMESTAMP, text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import PrimaryKeyConstraint
import sqlalchemy.orm

Base = sqlalchemy.orm.declarative_base()

class Comp(Base):
    __tablename__ = 'comp'
    name = Column(String(100))
    url = Column(String(200), nullable=False, unique=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    location = Column(String(100))
    organizer = Column(String(100))
    create_time = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    checked = Column(Integer, nullable=False, default=0)
    __table_args__ = (
        PrimaryKeyConstraint('url', name='url'),
        Index('idx_comp_create_time', 'create_time'),
    )
    mysql_charset = 'utf8mb4'

    def __init__(self, name, url, start_time=None, end_time=None, location=None, organizer=None):
        self.name = name
        self.url = url
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.organizer = organizer
        self.checked = 0

    def __str__(self):
        return str(self.name + " " + self.url + "\n")