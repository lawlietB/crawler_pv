import os
import re
import time
import requests
from bs4 import BeautifulSoup

f = open("link_product.txt","a")

catalog_list = [
    'https://phongvu.vn/may-tinh-ban.cat',
    'https://phongvu.vn/laptop.cat',
    'https://phongvu.vn/linh-kien-may-tinh.cat',
    'https://phongvu.vn/man-hinh-may-tinh.cat',
    'https://phongvu.vn/tivi.cat',
    'https://phongvu.vn/chuot-ban-phim-ban-di.cat',
    'https://phongvu.vn/dien-thoai-may-tinh-bang.cat',
    'https://phongvu.vn/thiet-bi-am-thanh.cat',
    'https://phongvu.vn/thiet-bi-van-phong.cat',
    'https://phongvu.vn/phu-kien.cat',
]

def getLinkProduct(url):
    code = requests.get(url)
    plaintext = code.text
    s = BeautifulSoup(plaintext, "html.parser")
    for link in s.findAll('a',{'class':'grid-view-item'}):
        product_link = link.get('href')
        print product_link
        f.write(product_link)
        f.write("\n")


def getAllCatalogPage(url):
    code = requests.get(url)
    plaintext = code.text
    s = BeautifulSoup(plaintext, "html.parser")

    url_current_page = url
    url_next_page = s.find('a',{'class':'next'}).get('href')

    print "URL current page: " + url_current_page
    getLinkProduct(url_current_page)

    if(url_current_page != url_next_page):
        getAllCatalogPage(url_next_page)


print "---Start getting link product---"
for catalog in catalog_list:
    print "==========================="
    print "Catalog URL: " + catalog
    print "==========================="    
    getAllCatalogPage(catalog)

f.close()