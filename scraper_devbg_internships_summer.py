import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://dev.bg/company/jobs/junior-intern/?_job_location=sofiya%2Cremote&_seniority=intern"

# Send HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all 'a' tags (which define hyperlinks) in the HTML
links = soup.find_all("a")

# Open a CSV file to write the links
with open("devbg_links_summer.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Title", "Link"])

    # Loop through the 'a' tags
    for link in links:
        href = link.get("href")
        # If the link contains "stazh" or "intern", check the linked page
        if href and ("stazh" in href or "intern" in href):
            # Send HTTP request to the linked page
            linked_page_response = requests.get(href)
            # Parse the HTML content of the linked page with BeautifulSoup
            linked_page_soup = BeautifulSoup(
                linked_page_response.content, "html.parser"
            )
            # Find all 'p' tags in the HTML
            paragraphs = linked_page_soup.find_all("p")
            # Keywords
            keywords = [
                "summer",
                "3-month",
                "3 months",
                "3 month",
                "june",
                "july",
                "october",
                "week",
                "юни",
                "юли",
                "октомври",
                "седмици",
            ]
            # Loop through the 'p' tags
            for paragraph in paragraphs:
                # If the paragraph contains "June", "summer", "3-month", "3 months", or "3 month"
                if any(keyword in paragraph.text.lower() for keyword in keywords):
                    # Find the 'h1' tag in the HTML
                    h1_tag = linked_page_soup.find("h1")
                    # If the 'h1' tag is found, write the link and the 'h1' content to the CSV
                    if h1_tag:
                        writer.writerow([h1_tag.text, href])
                    else:
                        print("No h1 tag found on page {}".format(href))
                    break
