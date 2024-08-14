# coding: utf-8
from sqlalchemy import Column, Float, Index, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
metadata = Base.metadata



class Conference(Base):
    __tablename__ = 'Conference'

    id = Column(String(50), primary_key=True)
    name = Column(String(255), nullable=False)
    other_name = Column(String(255))
    home_link = Column(String(255))
    ccf = Column(String(255))
    dblp = Column(String(255))
    full_name = Column(String(255))
    sub = Column(String(255))
    remark = Column(String(1000))


class ConferenceDetail(Base):
    __tablename__ = 'ConferenceDetail'

    id = Column(String(50), primary_key=True, nullable=False)
    year = Column(INTEGER(11), primary_key=True, nullable=False)
    link = Column(String(255))
    timezone = Column(String(255))
    abstract_deadline = Column(String(255))
    deadline = Column(TIMESTAMP)
    extended_deadline = Column(String(255))
    place = Column(String(255))
    date = Column(TIMESTAMP)
    acceptance_rate = Column(Float)
    remark = Column(String(1000))

class Journal(Base):
    __tablename__ = 'Journal'

    id = Column(String(50), primary_key=True)
    name = Column(String(255), nullable=False)
    ccf = Column(String(255))
    jcr = Column(String(255))
    cas = Column(String(255))
    _if = Column('if', String(255))
    full_name = Column(String(255))
    dblp = Column(String(255))
    home_link = Column(String(255))
    submission = Column(String(255))
    page = Column(INTEGER(11))
    acceptance_rate = Column(Float)
    review_duration = Column(Float)
    remark = Column(String(1000))

def initDB(sql_url):
    # 创建一个内存中的 SQLite 数据库
    if os.path.exists("./cli/sql.setting"):
        f = open("./cli/sql.setting", "r")
        engine = create_engine(open("./cli/sql.setting", "r").read(), echo=True)
    else:
        engine = create_engine(sql_url, echo=True)
    
    # 创建会话
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

