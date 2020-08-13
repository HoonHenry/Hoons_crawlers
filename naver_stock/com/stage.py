# combine all function and run the code
from libs.stock_crawl_func import get_company_info
from libs.stock_crawl_func import stock_code
from libs.stock_crawl_func import call_excel
from libs.stock_crawl_func import saver
from libs.stock_crawl_func import loader


code_lists = call_excel()
for code in code_lists:
    print(get_company_info(stock_code(code)))

