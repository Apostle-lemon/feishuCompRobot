from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml
from internal.pkg.logger import logger
from model.model import Race

with open('configs/config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

host = data['db']['host']
port = data['db']['port']
user = data['db']['user']
password = data['db']['password']
database = data['db']['dbName']
logger.info('mysql+mysqlconnector://' + user + ':' + password + '@' + host + ':' + port + '/' + database+'?charset=utf8')
engine = create_engine('mysql+mysqlconnector://' + user + ':' + password + '@' + host + ':' + port + '/' + database+'?charset=utf8')
Race.__table__.create(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()
logger.info("db connect success")