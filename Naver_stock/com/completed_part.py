from libs.crawl_func_complete import get_company_info
from libs.crawl_func_complete import call_excel
from libs.crawl_func_complete import stock_code


code_lists = call_excel()
for code in code_lists:
    print(get_company_info(stock_code(code)))

