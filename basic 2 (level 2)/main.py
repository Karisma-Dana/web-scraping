# scraping a job website for job listings

from bs4 import BeautifulSoup
import requests

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35&clusterName=CLUSTER_FA"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")
job_list = soup.find_all("li", class_="clearfix")
for job in job_list:
    # get a job title---
    job_titel = job.find("h2", class_="heading-trun")
    title = job.find("a").text.replace(" ", "")
    # company name
    company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
    # place
    place = job.find("li", class_="srp-zindex").text.replace(" ", "")

    print(
        f"""
    job title = {title}
    from company = {company_name}
    work in = {place}
    """
    )
