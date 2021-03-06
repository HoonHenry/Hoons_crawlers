import requests
from bs4 import BeautifulSoup as soup


LIMIT = 50


def get_last_pages(url):
    result = requests.get(url)
    parsing = soup(result.text, 'html.parser')
    pagination = parsing.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    print(max_page)
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    if company is not None:
        company_anchor = company.find("a")
        if company:
            if company_anchor is not None:
                company = str(company.find("a").string)
            else:
                company = str(company.string)
            company = company.strip()
        else:
            company = None
    else:
        company = "Unknown"

    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {"title": title, "company": company,
            "location": location,
            "link": f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_pages, url):
    jobs = []
    for page in range(last_pages):
        print(f"Scrapping indeed page {page+1}")
        result = requests.get(f"{url}&start={page*LIMIT}")
        parsing = soup(result.text, 'html.parser')
        results = parsing.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://www.indeed.com/jobs?q={word}&limit={LIMIT}"
    last_page = get_last_pages(url)
    jobs = extract_jobs(last_page, url)
    return jobs
