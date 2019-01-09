#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import re
import time
import requests
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def getData(url):
    code = requests.get(url)
    plaintext = code.text
    s = BeautifulSoup(plaintext, "html.parser")
    
    name = s.find('h1',{'class':'detail-product-name'}).get_text()
    
    price = s.find('span',{'class':'detail-product-final-price'}).get_text().replace(".","").strip()
    price = price[:-1]
    price = price.strip()
    
    images = []
    for image in s.findAll('img',{'class':'detail-gallery-img-item'}):
        images.append(image.get('src'))


    labels = []
    for label in s.findAll('th',{'class':'attribute-label'}):
        labels.append(label.get_text())

    values = []
    for value in s.findAll('td',{'class':'attribute-value'}):
        values.append(value.get_text())

    numOfAttribute = len(labels)
    
    print name
    # print price
    # for image in images:
    #     print image
    # for i in range(numOfAttribute):
    #     print labels[i] + values[i]

    fw = open("data.csv","a+")
    fw.write(name + ",")
    fw.write(price + ",")
    for image in images:
        fw.write(image + ":::")
    fw.write(",")
    for i in range(numOfAttribute):
        fw.write(labels[i].replace(",","").replace(";","") + values[i].replace(",","").replace(";","") + ":::")
    fw.write("\n")
    fw.close()



print "Start getting data"

f = open("link_product.txt","r")
for link in f:
    getData(link.strip())

f.close()