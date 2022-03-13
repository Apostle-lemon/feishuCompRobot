#!/usr/bin/python

import json
import requests
from bs4 import BeautifulSoup

cList = []
target_url = "https://www.huixx.cn/sai/match/index/profession/1/province/0/foreign/0/process/0/obj/0"

pageMax = 2; # 爬几页

head = {
    'Cookie': 'tab_obj_index=-1; tab_obj_index=-1; PHPSESSID=ec71dda31ab00e6f76dd2ab6182b6510; googlespider=u%C5%86%ACGb%E3%E9%12%60%B4%81%3A%0D%BF%ED2cS%23%A9x%07K%294u%B3%87%F0n%09%EFy%FE%9D%F6%F5%B9%FA%7DN%C9%BFC%CE%AA%87%DB%DF%9D%DC%B0%00%5C%852vX%C50%F8%8C%EB%17%BE%82%1F%0C%7C%1E%D6%D00%D1%24%0BO%DF%29%F3%89%29%0A%9A%21Q%9F%C7X%0E%9AAb%BEx%D6%03%AA%14%B5%DA%BE%93%17%E6%2C%AA%9A%3E3%13%0B%D3I%28LTwj%5B%98%60%23%5C%8D%0D%22',
}

s = requests.session()

class CInfo :
    def __init__(self, url, name, sTime, cTime, status) :
        self.url = "https://www.huixx.cn"+ url.strip()                  # info msg url
        self.name = name.strip()                                        # competition name
        self.sTime = sTime                                              # sign up time
        self.cTime = cTime                                              # competing time
        # self.status = status.strip()                                    # competition status
        self.source = ''
        try:
            self.source = requests.get(self.url,headers = head).text        # get info msg
        except requests.exceptions.ConnectTimeout or requests.exceptions.ProxyError:
            print("Cinfo url" + str(url) + "Error")
        self.bsobj = BeautifulSoup(self.source, features = "lxml")
        self.details = self.bsobj.find_all(is_details)
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

def getLastUpdTime() :
    f = open('./tmp/_huixx.cn_.tmp','r')
    time = f.read()
    f.close()
    return time

def updUpdTime(time) :
    f = open("./tmp/_huixx.cn_.tmp",'w')
    f.write(time)
    f.close()
    return

def main() :
    lastUpdTime = getLastUpdTime()
    newUpdTime = lastUpdTime 
    # initialize POST body
    # 初始化 POST 请求体
    body = []
    for i in range(pageMax) :
        body.append({ 'profession_arr[]': '1', 'page': str(i+1) })

    
    try:
        resp = s.get(target_url,headers = head)
    except requests.exceptions.ConnectTimeout or requests.exceptions.ProxyError or requests.exceptions.ConnectionError :
        print("Error, check the proxy first, then contact the software team")
    for i in range(pageMax) :
        try:
            resp = s.post(target_url,headers = head,data = body[i])
        except requests.exceptions.ConnectTimeout or requests.exceptions.ProxyError or requests.exceptions.ConnectionError :
            print("Error, check the proxy first, then contact the software team")
        jsonStr = json.loads(resp.text[71:]).get('data').get('list')
        for j in range(15) : # 一页有十五项
            updTime = ''
            url = name = sTime = cTime = status = ""
            
            updTime = jsonStr[j].get('update_time')
            
            if updTime < lastUpdTime :
                continue

            if updTime > newUpdTime :
                newUpdTime = updTime
            
            url = "/match_" + str(jsonStr[j].get('id'))
            name = jsonStr[j].get('name')
            status = str(jsonStr[j].get('process_name'))
            sTime = [str(jsonStr[j].get('start_pre_time')).strip(), str(jsonStr[j].get('end_pre_time')).strip()]
            cTime = [str(jsonStr[j].get('start_time')).strip(), str(jsonStr[j].get('end_time')).strip()]
            newCmpt = CInfo(url, name, sTime, cTime, status)
            cList.append( newCmpt )     # 所有比赛信息都在该 list 中
            
            # newCmpt.printMe()           # 打印比赛信息
    updUpdTime(newUpdTime)

if __name__ == "__main__" :
    main()
