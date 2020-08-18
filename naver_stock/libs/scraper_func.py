import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def get_company_info(code):
    # crawling --> http request
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    data = requests.get(url)
    obj = BeautifulSoup(data.content, "html.parser")
    # find the company name
    wrap_company = obj.find("div", {"class": "wrap_company"})
    name = wrap_company.find("a").text

    # price
    today = obj.find("div", {"class": "today"})
    price = today.find("span", {"class": "blind"}).text

    info_table = obj.find('table', {'class': 'no_info'}).findAll('tr')
    first_row = info_table[0].findAll('span', {'class': 'blind'})
    second_row = info_table[1].findAll('span', {'class': 'blind'})

    # high, low, start, yesterday, exchange_volume, transaction_price
    yesterday, high = first_row[0].text, first_row[1].text
    volume, start, = first_row[3].text, second_row[0].text
    low, trans = second_row[1].text, second_row[2].text

    return {"name": name, "price": price, "high": high, "low": low, "start": start,
            "yesterday": yesterday, "volume": volume, "transaction": trans}


def stock_code(code):
    recoded = str(code)
    if len(recoded) != 6:
        return "0" * (6 - len(recoded)) + recoded
    return recoded


def call_excel():
    # excel = pd.read_html(r"/home/hoons/hoons_code/Hoons_crawlers/naver_stock/libs/KOSPI.xls")
    # print(excel.head())
    # excel.to_csv(r"/home/hoons/hoons_code/hoons_nlp_prac/stock_crawl/libs/KOSPI_auto.csv", index=None, header=True)
    loc = r"/home/hoons/hoons_code/hoons_nlp_prac/stock_crawl/libs/KOSPI_manual.csv"
    file = pd.read_csv(loc)
    # print(len(file["종목코드"]))
    return [file["종목코드"][i] for i in range(len(file["종목코드"][0:3]))]


def saver(dictex):
    for key, val in dictex.items():
        val.to_csv("data_{}.csv".format(str(key)))

    with open("keys.txt", "w") as f: #saving keys to file
        f.write(str(list(dictex.keys())))


def loader():
    """Reading data from keys"""
    with open("keys.txt", "r") as f:
        keys = eval(f.read())

    dictex = {}
    for key in keys:
        dictex[key] = pd.read_csv("data_{}.csv".format(str(key)))

    return dictex


