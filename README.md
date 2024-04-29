<p align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white">
<img src="https://dev.bg/wp-content/uploads/2021/12/cropped-dev.bg-logo.png" alt="DEV.BG" class="dev-bg-logo" width="121" height="24">
<img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
</p>

# Web Scraper for Internships Sofia

These scripts are web scrapers that search for internship links on LinkedIn and Dev.bg. The results are saved in a CSV file.
There are 4 different scripts, 2 for linkedin and 2 for dev.bg. The two types differ by keywords, some include keywords for summer-only internships, others don't.

## Installation

To run this script, you need Python (tested on 3.12) and the following packages:

- BeautifulSoup
- pandas
- requests
- csv

You can install these packages using pip:

```bash
pip install beautifulsoup4 requests pandas
```

## Cloning the Repository
```bash
git clone https://github.com/dobval/Sofia-Summer-Internship-Webscraper-LinkedIn-Devbg.git
cd Sofia-Summer-Internship-Webscraper-LinkedIn-Devbg
```

## Usage

To use this script, simply run it with Python, for example:

```bash
python scraper_linkedIn_internships_summer.py
```

The script will create a CSV file named `linkedin_links_summer.csv` in the same directory. This file will contain the titles and links from the linked pages that contain (and exclude) the specified keywords.

### Example CSV
![image](https://github.com/dobval/Sofia-Summer-Internship-Webscraper-LinkedIn-Devbg/assets/100198047/e3aa376c-acef-487d-8996-6825b0334e49)


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
