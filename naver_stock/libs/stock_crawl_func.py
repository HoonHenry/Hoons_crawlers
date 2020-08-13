import requests
from bs4 import BeautifulSoup
import pandas as pd


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

    # high


    # low


    return {"name": name, "price": price, "high": "", "low": ""}


def stock_code(code):
    recoded = str(code)
    if len(recoded) != 6:
        return "0" * (6 - len(recoded)) + recoded
    return recoded


def call_excel():
    excel = pd.read_html(r"/home/hoons/hoons_code/hoons_nlp_prac/stock_crawl/libs/KOSPI.xls")
    print(excel.head())
    # excel.to_csv(r"/home/hoons/hoons_code/hoons_nlp_prac/stock_crawl/libs/KOSPI_auto.csv", index=None, header=True)
    # loc = r"/home/hoons/hoons_code/hoons_nlp_prac/stock_crawl/libs/KOSPI_manual.csv"
    # file = pd.read_csv(loc)
    # print(len(file["종목코드"]))
    # return [file["종목코드"][i] for i in range(len(file["종목코드"][0:3]))]
    return 0


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