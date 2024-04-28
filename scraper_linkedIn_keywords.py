import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://bg.linkedin.com/jobs/internship-jobs-sofia?original_referer=https%3A%2F%2Fwww.qwant.com%2F&position=1&pageNum=0"
response = requests.get(url)

data = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("div", {"class": "job-search-card"})
    for job in job_listings:
        title = job.find("h3", {"class": "base-search-card__title"}).text.strip()
        company = job.find("a", {"class": "hidden-nested-link"}).text.strip()
        location = job.find("span", {"class": "job-search-card__location"}).text.strip()
        anchor_tag = job.find("a", class_="base-card__full-link")
        href_link = anchor_tag["href"]

        # Make a request to the individual job page
        job_response = requests.get(href_link)
        time.sleep(2)  # Add a delay of 2 seconds to prevent IP Blocking from LinkedIn
        if job_response.status_code == 200:
            job_soup = BeautifulSoup(job_response.text, "html.parser")
            description = job_soup.find(
                "div",
                {
                    "class": "show-more-less-html__markup show-more-less-html__markup--clamp-after-5 relative overflow-hidden"
                },
            ).text.strip()

            # Check if the description contains the keywords, exlude non-summer internships
            keywords = ["summer", "June", "3-month"]
            excluded_keywords = ["6 month", "9 month"]
            if any(keyword in description for keyword in keywords) and not any(
                excluded_keyword in description
                for excluded_keyword in excluded_keywords
            ):
                data.append([title, company, location, href_link])

    df = pd.DataFrame(data, columns=["Title", "Company", "Location", "Link"])
    df.to_csv("internshipdata.csv", index=False)

else:
    print("Failed to fetch job listings.")
