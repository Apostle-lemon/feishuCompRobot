import requests
import datetime
from bs4 import BeautifulSoup
import lxml
import os

pageMax = 5
cTypes = {"commerce", "colligate"}
headers = {'User-Agent': "my-app/0.0.1"}
cList = []
path = os.getcwd() + '\\' + "detail"


def creatFile(path,name,url):
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            resp = requests.get(url, headers=headers, timeout=3)
            soup = BeautifulSoup(resp.text, 'lxml')
            file = open(path + '/' + name + ".html", 'w', encoding='utf-8')
            file.write(str(soup))
            file.close()
        except requests.exceptions.ConnectTimeout or requests.exceptions.ProxyError:
            print("Cinfo url" + str(url) + "Error")

class CInfo:
    def __init__(self, url, name, sTime, cTime, status):
        self.url = url
        self.name = name.strip()  # competition name
        self.sTime = sTime  # sign up time
        self.cTime = cTime  # competing time
        self.status = status.strip()  # competition status
        creatFile(path,self.name,self.url)
        pass

    def printMe(self):
        print(self.url, end="\n")
        print(self.name, end="\n")
        print(self.sTime, end="\n")
        print(self.cTime, end="\n")
        print(self.status, end="\n\n")


def main():
    for cType in cTypes:
        baseurl = "https://www.saikr.com/vs/" + cType + "/0/0?page="
        for page in range(pageMax):
            try:
                resp = requests.get(baseurl + str(page + 1), headers=headers, timeout=3)
            except requests.exceptions.ConnectTimeout or requests.exceptions.ProxyError or requests.exceptions.ConnectionError:
                print("Error, check the proxy first, then contact the software team")
            soup = BeautifulSoup(resp.text, "lxml")
            listItem = soup.find_all("li")
            print("\n\ndetail .html in" + path+'\n\n')
            for i in listItem:
                if i.has_attr("class") and i.attrs['class'] == ["item", "clearfix"]:
                    name = i.find(class_="link").string
                    sTime = i.find_all(class_="event4-1-plan")[2].text[4:]
                    cTime = i.find_all(class_="event4-1-plan")[3].text[4:].strip()
                    statue = i.find('em').text.strip()
                    url = i.find_all("a")[-1:][0].attrs["href"]
                    newCmpy = CInfo(url, name, sTime, cTime, statue)
                    cList.append(CInfo)
                    newCmpy.printMe()


if __name__ == '__main__':
    main()
