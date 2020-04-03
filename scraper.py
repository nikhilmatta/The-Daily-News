#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:11:14 2020

@author: nikhilmatta
"""

import requests
from bs4 import BeautifulSoup
import re

data={'links':[],'headline':[],'image':[],'category':[],'date':[],'article':[],'summary':[],'sentiment':[]}
#df = pd.DataFrame(columns = ['links','image','category','date','article','summary','sentiment'])
headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15.3; rv:42.0) Gecko/20100101 Firefox/28.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest'
        }
    
def getLinks():
    for i in range(2,4):
        try:    
            r=requests.get('https://www.hindustantimes.com/latest-news/?pageno='+str(i),headers=headers)
            soup=BeautifulSoup(r.content,"lxml")
            try:
                for url in soup.findAll("a",{"title":"read more"}):
                    if url['href'] not in data['links']:
                        data['links'].append(url["href"])
            except:pass
        except:pass

def getArticleData():
    for i in range(len(data['links'])):
        try:
            r=requests.get(data["links"][i],headers=headers)
            soup=BeautifulSoup(r.content,"lxml")
            try:
                data['headline'].append(soup.find("h1").getText())
            except:
                data['headline'].append("")
            try:
                data['category'].append(soup.find("span",{"class":"cta-link lok-sabha-elections-cb-sectionmr-15"}).getText())
            except:
                data['category'].append("")
            try:
                data['date'].append(soup.find("span",{"class":"text-dt"}).getText())
            except:
                data['date'].append("")
            try:
                data['image'].append(soup.find('img', {'src':re.compile('.jpg')}).get('src'))
            except:
                data['image'].append("")
            txt=""
            try:
                for s in soup.find("div",{"class":"storyDetail"}).findAll("p"):
                    txt=txt+s.getText()
                #print(txt)
                data['article'].append(str(txt))
            except:
                data['article'].append(str(txt))
        except:pass

#df=pd.DataFrame.from_dict(data)
    