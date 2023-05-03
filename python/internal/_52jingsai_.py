import requests
from .comp_list import compList
from bs4 import BeautifulSoup
from .pkg.logger import logger
from model.model import Comp

compType = ['shangyechuangye','keji','xkjn']
pageMax = [2, 2, 2]  # 对于 商业创业，科技，学科竞赛 分别爬几页
target_url = 'http://www.52jingsai.com/bisai/'


def is_list(tag):
    return tag.has_attr('class') and tag['class'] == ['xld']


def is_comp(tag):
    return tag.has_attr('class') and tag['class'] == ['bbda', 'list_bbda', 'cl']


def main():
    for i in range(3):
        for page in range(pageMax[i]):
            pageInfo = {'page': str(page + 1)}
            try:
                logger.info(target_url + compType[i] + 'index.php?'+str(pageInfo))
                resp = requests.get(target_url + compType[i], params=pageInfo)
            except:
                logger.error("Error, check the proxy first, then contact the software team")
                continue
            logger.info('get 52jingsai successfully done')
            bsobj = BeautifulSoup(resp.text, features='lxml')
            for comp in bsobj.find(is_list).find_all(is_comp):
                name = comp.find('dt', class_='xs2_tit').a.text.strip()
                link = comp.find('a').get('href')
                url = 'http://www.52jingsai.com/' + link.strip()
                newcomp = Comp(name,url)
                compList.append(newcomp)


if __name__ == "__main__":
    main()
