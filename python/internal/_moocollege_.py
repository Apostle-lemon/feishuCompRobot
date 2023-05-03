from model.model import Comp
from .pkg.logger import logger
import requests
from bs4 import BeautifulSoup
from .comp_list import compList

headers = {'User-Agent': "my-app/0.0.1"}

def main():
    null = None
    true = True
    false = False
    logger.info("Start enumming moocollege")
    try:
        resp = requests.get("https://cc.moocollege.com/api/web/selectCompetitionInfoList?type=0&status=1&pageNum=1&pageSize=100000",
        headers=headers, timeout=30)
    except:
        logger.error("While enumming pages : Error, check the proxy first, then contact the software team")
        return
    logger.info('get moocollege successfully done')
    datalist = eval(resp.text).get("data").get("list")
    for data in datalist:
        try:
            name = data.get("name")
            url = data.get("url")
            if url == None:
                url = "https://cc.moocollege.com/#/details?" + str(data.get("id"))
            newCompetition = Comp(name,url)
            compList.append(newCompetition)
        except:
            logger.error("data structure error, maybe the website has changed the structure")
            continue


if __name__ == '__main__':
    main()
