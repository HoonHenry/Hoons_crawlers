from naver_stock.libs.scraper_func import (get_company_info, call_excel, stock_code, saver)


code_lists = call_excel()
stock_list = []
for code in code_lists:
    stock_list.append(get_company_info(stock_code(code)))

saver(stock_list)
