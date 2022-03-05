#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

class CInfo :
    def __init__(self, url, name, sTime, cTime, status) :
        self.url = "https://www.huixx.cn"+ url.strip()  # info msg url
        self.name = name.strip()                        # competition name
        self.sTime = sTime.strip()                      # sign up time
        self.cTime = cTime.strip()                      # competing time
        self.status = status.strip()                    # competition status
        self.source = requests.get(self.url) .text      # get info msg
        bsobj = BeautifulSoup(self.source, features = "lxml")
        texts = bsobj.find(is_details)
        self.details = texts
        pass
    def printMe(self) :
        print(self.url, end="\n")
        print(self.name, end="\n")
        print(self.sTime, end="\n")
        print(self.cTime, end="\n")
        print(self.status, end="\n")
        print(self.details)

def is_details(tag) :
    return tag.has_attr('class') and tag['class'] == ["bg-ff", "pl-30", "pr-30", "pt-20", "pb-25", "mb-20", "rich_text"] 

def is_competition_record(tag) :
    return tag.has_attr('class') and tag['class'] == ["bor_bda", "pl-5"]

def main() :
    # 创业营商 + 慧查查
    url = "https://www.huixx.cn/sai/match/index/profession/1/province/0/foreign/0/process/0/obj/0"
    resp = requests.get(url)
    bsobj = BeautifulSoup(resp.text, features = "lxml")
    cList = []
    for cpt in bsobj.find_all(is_competition_record) :
        url = name = sTime = cTime = status = ""
        for link in cpt.find_all('a') :
            url = link.get("href")
            name = link.string
        for rec in cpt.find_all('span') : 
            str = rec.string
            if str[0] == "报" :
                sTime = str
            if str[0] == "比" : 
                cTime = str
            if str[0] == "赛" : 
                status = str
        newCmpt = CInfo(url, name, sTime, cTime, status)
        cList.append( newCmpt ) 
        newCmpt.printMe()
        exit()

if __name__ == "__main__" :
    main()
