from internal.get_all_comp import main as getAllcomp
from internal.comp_list import compList
from internal.store.connect import Session
from model.model import Comp
from internal.pkg.logger import logger
import datetime

def main():
    getAllcomp()
    for compItem in compList:
        add_comp(compItem)
    logger.info("All Done in current time: " + str(datetime.datetime.now()))
    # 清空 compList
    compList.clear()

def add_comp(compItem):
    # print(comp)
    session = Session()
    exists = session.query(Comp).filter_by(url=compItem.url).first()
    if exists:
        logger.debug("find the same url:" + compItem.url)
        session.close()
        return
    session.add(compItem)
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