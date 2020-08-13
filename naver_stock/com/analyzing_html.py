import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"
web = requests.get(url)
obj = BeautifulSoup(web.content, "html.parser")
# print(obj)
table = obj.find("table", {"class": "no_info"})
print(table)
infos = table.findAll("span", {"class": "blind"})
# print([x.text for x in infos])
