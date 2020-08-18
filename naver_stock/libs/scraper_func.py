import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


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
    loc = r"D:\hoons_code\Hoons_crawlers\naver_stock\libs\KOSPI_manual.csv"
    file = pd.read_csv(loc)
    print(len(file["종목코드"]))
    return [file["종목코드"][i] for i in range(len(file["종목코드"][0:30]))]


def saver(stock_lists):
    file = open("stocks.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["name", "price", "high", "low", "start",
                     "yesterday", "volume", "transaction"])
    for stock in stock_lists:
        writer.writerow(list(stock.values()))
    return 0

#
# def show_process(nums):
#     for i in range(1,101):
#         print("_"*20)