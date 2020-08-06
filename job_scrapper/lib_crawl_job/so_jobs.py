import requests
from bs4 import BeautifulSoup as soup


URL = f"https://stackoverflow.com/jobs?pg="


def get_last_page():
    result = requests.get(URL)
    parse = soup(result.text, "html.parser")
    pages = parse.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    print(last_page)
    return int(last_page)


def extract_job(html):
    title = html.find("h2").text.strip()
    company, location = html.find("h3",
                            {"class": "fs-body1"}).find_all("span",
                                                            recursive=False)
    company = company.get_text(strip=True)      # do extra strip if exists
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    return {"title": title, "company": company,
            "location": location,
            "apply_link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Stackoverflow page {page}")
        result = requests.get(f"{URL}{page+1}")
        parse = soup(result.text, "html.parser")
        results = parse.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            # print(job)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
