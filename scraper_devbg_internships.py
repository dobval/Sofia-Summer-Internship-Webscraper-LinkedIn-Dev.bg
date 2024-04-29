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
with open("devbg_links.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Link"])

    # Loop through the 'a' tags
    for link in links:
        href = link.get("href")
        # If the link contains "stazh" or "intern", write it to the CSV
        if href and ("stazh" in href or "intern" in href):
            writer.writerow([href])
