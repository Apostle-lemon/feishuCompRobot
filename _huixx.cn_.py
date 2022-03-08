#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
headers = {
    'Cookie': 'tab_obj_index=-1; PHPSESSID=ec71dda31ab00e6f76dd2ab6182b6510; googlespider=u%C5%86%ACGb%E3%E9%12%60%B4%81%3A%0D%BF%ED2cS%23%A9x%07K%294u%B3%87%F0n%09%EFy%FE%9D%F6%F5%B9%FA%7DN%C9%BFC%CE%AA%87%DB%DF%9D%DC%B0%00%5C%852vX%C50%F8%8C%EB%17%BE%82%1F%0C%7C%1E%D6%D00%D1%24%0BO%DF%29%F3%89%29%0A%9A%21Q%9F%C7X%0E%9AAb%BEx%D6%03%AA%14%B5%DA%BE%93%17%E6%2C%AA%9A%3E3%13%0B%D3I%28LTwj%5B%98%60%23%5C%8D%0D%22',
}
class CInfo :
    def __init__(self, url, name, sTime, cTime, status) :
        self.url = "https://www.huixx.cn"+ url.strip()                  # info msg url
        self.name = name.strip()                                        # competition name
        self.sTime = sTime.strip()                                      # sign up time
        self.cTime = cTime.strip()                                      # competing time
        self.status = status.strip()                                    # competition status
        self.source = requests.get(self.url,headers = headers).text     # get info msg
        self.bsobj = BeautifulSoup(self.source, features = "lxml")
        self.details = self.bsobj.find_all(is_details)
        pass
    def printMe(self) :
        print(self.url, end="\n")
        print(self.name, end="\n")
        print(self.sTime, end="\n")
        print(self.cTime, end="\n")
        print(self.status, end="\n")
        print(self.details[0], end="\n")
        print(self.details[1], end="\n")

def is_details(tag) :
    return tag.has_attr('class') and tag['class'] == ["bg-ff", "pl-30", "pr-30", "pt-20", "pb-25", "mb-20", "rich_text"] 

def is_competition_record(tag) :
    return tag.has_attr('class') and tag['class'] == ["bor_bda", "pl-5"]

def main() :
    # 创业营商 + 慧查查
    url = "https://www.huixx.cn/sai/match/index/profession/1/province/0/foreign/0/process/0/obj/0"
    headers = {
        # 假装自己是浏览器
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.12 Safari/537.36',
        # 把你刚刚拿到的Cookie塞进来
        'Cookie': 'tab_obj_index=-1; PHPSESSID=ec71dda31ab00e6f76dd2ab6182b6510; googlespider=u%C5%86%ACGb%E3%E9%12%60%B4%81%3A%0D%BF%ED2cS%23%A9x%07K%294u%B3%87%F0n%09%EFy%FE%9D%F6%F5%B9%FA%7DN%C9%BFC%CE%AA%87%DB%DF%9D%DC%B0%00%5C%852vX%C50%F8%8C%EB%17%BE%82%1F%0C%7C%1E%D6%D00%D1%24%0BO%DF%29%F3%89%29%0A%9A%21Q%9F%C7X%0E%9AAb%BEx%D6%03%AA%14%B5%DA%BE%93%17%E6%2C%AA%9A%3E3%13%0B%D3I%28LTwj%5B%98%60%23%5C%8D%0D%22',
    }
    
    
    resp = requests.get(url,headers = headers)
    bsobj = BeautifulSoup(resp.text, features = "lxml")

    cList = []
    
    for cpt in bsobj.find_all(is_competition_record) :
        url = name = sTime = cTime = status = ""

        # 获取列表内目标比赛的网址
        for link in cpt.find_all('a') :
            url = link.get("href")
            name = link.string

        # 获取列表内显示的比赛信息
        for rec in cpt.find_all('span') : 
            str = rec.string
            if str[0] == "报" :
                sTime = str
            if str[0] == "比" : 
                cTime = str
            if str[0] == "赛" : 
                status = str
        # 初始化一个比赛对象，并在构造函数内部获得比赛详细信息
        newCmpt = CInfo(url, name, sTime, cTime, status)
        cList.append( newCmpt )  # 所有比赛信息都在该 list 中
        # newCmpt.printMe()   # 打印比赛信息
    exit()

if __name__ == "__main__" :
    main()
