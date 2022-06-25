from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def get_job_data(job_keywords, location):
    '''This function gets indeed data and returns the listing text'''

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }

    job_keywords = ['data', 'engineer']
    location =  'United+States'
    joined_keywords = '+'.join(job_keywords)

    url = f"https://www.indeed.com/jobs?q={joined_keywords}&l={location}"
    api_url = "https://www.indeed.com/viewjob?viewtype=embedded&jk={job_id}"

    soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")


    job_listing = {}

    for job in soup.select('a[id^="job_"]')[0:5]:
        job_id = job["id"].split("_")[-1]
        s = BeautifulSoup(
            requests.get(api_url.format(job_id=job_id), headers=headers).content,
            "html.parser",
        )
        
        job_listing[job_id] = s.title.get_text(strip=True) + s.select_one("#jobDescriptionText").get_text(strip=True, separator="\n")

    return job_listing
        # print(s.title.get_text(strip=True))
        # print()
        # print(
        #     s.select_one("#jobDescriptionText").get_text(strip=True, separator="\n")
        # )
        # print("#" * 80)