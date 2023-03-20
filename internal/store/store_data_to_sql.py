from internal.get_all_race import main as getAllRace
from internal.race_list import raceList
from internal.store.connect import Session
from model.model import Race
from internal.pkg.logger import logger
import datetime

def main():
    getAllRace()
    for race in raceList:
        add_race(race)
    logger.info("All Done in current time: " + str(datetime.datetime.now()))
    # 清空 raceList
    raceList.clear()

def add_race(race):
    # print(race)
    session = Session()
    exists = session.query(Race).filter_by(url=race.url).first()
    if exists:
        logger.debug("find the same url:" + race.url)
        session.close()
        return
    session.add(race)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error("Insert Error")
        logger.error(e)
    finally:
        session.close()


if __name__ == '__main__':
    main()