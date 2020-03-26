import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
from urllib.parse import urlparse

driver = webdriver.Chrome('/home/eunbi/Desktop/Study/크롤링/chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.kurly.com/shop/goods/goods_list.php?category=038')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
my_photos = soup.select(
    '#goodsList > div.list_goods > div > ul > li:nth-child(1) > div > div > a > img '
)
print(my_photos)
print('-----------------------------------')
for photos in my_photos:
    print(photos['src'])
    photo = photos['src']

urllib.request.urlretrieve(photo, "/home/eunbi/Desktop/Study/크롤링/image/test.jpg")