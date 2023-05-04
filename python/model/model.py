from sqlalchemy import Column, DateTime, Index, String, TIMESTAMP, text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import PrimaryKeyConstraint
import sqlalchemy.orm
from datetime import datetime, date, time, timedelta

day = date(1970, 5, 1)
time = time(0, 0)
defaultTime = datetime.combine(day, time)

Base = sqlalchemy.orm.declarative_base()

class Comp(Base):
    __tablename__ = 'comp'
    name = Column('name',String(100))
    url = Column('url',String(200), nullable=False, unique=True,primary_key=True)
    start_time = Column('start_time',DateTime)
    end_time = Column('end_time',DateTime)
    location = Column('location',String(100))
    organizer = Column('organizer',String(100))
    create_time = Column('create_time',TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    checked = Column('checked',Integer, nullable=False, default=0)
    __table_args__ = (
        PrimaryKeyConstraint('url', name='url'),
        Index('idx_comp_create_time', 'create_time'),
    )
    mysql_charset = 'utf8mb4'

    def __init__(self, name, url, start_time=defaultTime, end_time=defaultTime, location=None, organizer=None):
        self.name = name
        self.url = url
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.organizer = organizer
        self.checked = 0

    def __str__(self):
        return str(self.name + " " + self.url + "\n")