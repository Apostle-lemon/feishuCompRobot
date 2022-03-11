import requests
import datetime
from bs4 import BeautifulSoup
import lxml
import os

path = os.getcwd() + '\\' + "detail"


def creatFile(path, name, url):
    if not os.path.exists(path):
        os.makedirs(path)
    if (url is None):
        return
    try:
        resp = requests.get("http://" + url, headers=headers, timeout=3)
        soup = BeautifulSoup(resp.text, 'lxml')
        file = open(path + '/' + name + ".html", 'w', encoding='utf-8')
        file.write(str(soup))
        file.close()
    except requests.exceptions.ConnectTimeout or requests.exceptions.ProxyError:
        print("Cinfo url" + str(url) + "Error" + "connection failed")
    except requests.exceptions.MissingSchema:
        print("url Error " + str(url) + " Url invalid")


class CInfo:
    def __init__(self, url, name, sTime, eTime):
        self.url = url
        self.name = name.strip()
        self.sTime = sTime.strip()
        self.eTime = eTime.strip()
        # creatFile(path, self.name, self.url) not support
        pass

    def printMe(self):
        print(self.name, end="\n")
        print("URL = " + str(self.url), end="\n")
        print(self.sTime, end="----->")
        print(self.eTime, end="\n\n")


headers = {'User-Agent': "my-app/0.0.1"}

resp = requests.get(
    "https://cc.moocollege.com/api/web/selectCompetitionInfoList?type=0&status=1&pageNum=1&pageSize=100000",
    headers=headers, timeout=30)


def main():
    null = None
    false = False
    true = True
    datalist = eval(resp.text).get("data").get("list")
    cList = []
    for data in datalist:
        name = data.get("name")
        startTime = data.get("startTime")[0:10]
        endTime = data.get("endTime")[0:10]
        url = data.get("url")
        if url == None :
            url = "https://cc.moocollege.com/#/details?" + str(data.get("id"))
        newCompetition = CInfo(url, name, startTime, endTime)
        cList.append(newCompetition)
        newCompetition.printMe()


if __name__ == '__main__':
    main()
