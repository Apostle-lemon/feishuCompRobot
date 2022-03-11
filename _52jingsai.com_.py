#!/usr/bin/python

import json
import requests
from bs4 import BeautifulSoup

cList = []
target_url = 'http://www.52jingsai.com/bisai/shangyechuangye/chuangye/index.php?'
urlSufix = ['jsstatus=2', 'jsstatus=1', 'jsstatus=6']
cmptStatus = ['registering', 'before register', 'after register']

pageMax = [2, 1, 2]; # 爬几页

class CInfo :
    def __init__(self, url, status) :
        self.url = 'http://www.52jingsai.com/' + url.strip()        # info msg url
        self.status = status.strip()                                # competition status
        self.source = ''
        try:
            self.source = requests.get(self.url).text                   # get info msg
        except requests.exceptions.ConnectTimeout or requests.exceptions.ProxyError:
            print("Cinfo url" + str(url) + "Error")
        self.bsobj = BeautifulSoup(self.source, features = 'lxml')
        self.summary = self.bsobj.find(is_summary)
        self.details = []
        for msg in self.bsobj.find(is_details) :
            if( (not isinstance( msg, type('string') )) and msg.has_attr('class') and (msg['class'] == [ 'team' ] or msg['class'] == [ 'qqbg' ]) ) :
                continue
            self.details.append(msg)
    def printMe(self) :
        print(self.url, end="\n")
        print(self.summary, end="\n")
        for line in self.details :
            print(line, end="\n")

def is_details(tag) : 
    return tag.has_attr('id') and tag['id'] == 'article_content'

def is_summary(tag) :
    return tag.has_attr('class') and tag['class'] == [ 's', 'zhaiyao' ]

def is_list(tag) :
    return tag.has_attr('class') and tag['class'] == [ 'xld' ]

def is_cmpt(tag) :
    return tag.has_attr('class') and tag['class'] == [ 'bbda', 'list_bbda', 'cl' ]

def main() :
    for i in range(3) :
        for page in range(pageMax[i]) :
            pageInfo = { 'page': str(page+1) }
            try:
                resp = requests.get(target_url + urlSufix[i], params = pageInfo)
            except requests.exceptions.ConnectTimeout or requests.exceptions.ProxyError or requests.exceptions.ConnectionError :
                print("Error, check the proxy first, then contact the software team")
            bsobj = BeautifulSoup(resp.text, features = 'lxml')
            flag = True
            for cmpt in bsobj.find(is_list).find_all(is_cmpt) :
                flag = False
                link = cmpt.find('a').get('href')
                newCmpt = CInfo(link, cmptStatus[i])
                cList.append(newCmpt)
                newCmpt.printMe()
            if flag :
                break
if __name__ == "__main__" :
    main()