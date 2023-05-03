from model.model import Comp
from .pkg.logger import logger
import requests
from bs4 import BeautifulSoup
from .comp_list import compList

pageMax = 1
compTypes = {"engineering", "commerce", "colligate"}
headers = {'User-Agent': "my-app/0.0.1"}
compList = []

def main():
    for compType in compTypes:
        baseurl = "https://www.saikr.com/vs/" + compType + "/0/1?page="
        for page in range(pageMax):
            pageUrl = baseurl + str(page + 1)
            logger.info(pageUrl)
            try:
                resp = requests.get(pageUrl, headers=headers, timeout=3)
            except:
                logger.error("While enumming pages : Error, check the proxy first, then contact the software team")
                continue
            logger.info('get saikr successfully done')
            
            soup = BeautifulSoup(resp.text, "lxml")
            listItem = soup.find_all("li")
            for i in listItem:
                if i.has_attr("class") and i.attrs['class'] == ["item", "clearfix"]:
                    name = i.find(class_="link").string
                    url = i.find_all("a")[-1:][0].attrs["href"]
                    newcomp = Comp(name, url)
                    compList.append(newcomp)

if __name__ == '__main__':
    main()