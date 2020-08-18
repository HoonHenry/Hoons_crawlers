from naver_stock.libs.scraper_func import get_company_info
from naver_stock.libs.scraper_func import call_excel
from naver_stock.libs.scraper_func import stock_code


code_lists = call_excel()
for code in code_lists:
    print(get_company_info(stock_code(code)))
