# parser/job_sources.py

import requests
from bs4 import BeautifulSoup

def scrape_remoteok():
    jobs = []
    url = "https://remoteok.com"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")

    for row in soup.select("tr.job"):
        title = row.get("data-position")
        company = row.get("data-company")
        link = url + row.get("data-href", "")
        if title and company:
            jobs.append({
                "title": title,
                "company": company,
                "link": link
            })
    return jobs

def scrape_weworkremotely():
    jobs = []
    url = "https://weworkremotely.com/categories/remote-programming-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")

    for section in soup.select("section.jobs"):
        for li in section.select("li:not(.view-all)"):
            title_elem = li.select_one("span.title")
            company_elem = li.select_one("span.company")
            link_elem = li.find("a", href=True)
            if title_elem and company_elem and link_elem:
                jobs.append({
                    "title": title_elem.text.strip(),
                    "company": company_elem.text.strip(),
                    "link": "https://weworkremotely.com" + link_elem["href"]
                })
    return jobs
