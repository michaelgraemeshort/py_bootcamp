import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.rithmschool.com/blog"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_scraping_data.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(("title", "href", "time"))
    for article in articles:
        anchor_tag = article.find("a")
        title = anchor_tag.get_text()
        href = anchor_tag["href"]
        time = article.find("time")["datetime"]
        csv_writer.writerow((title, href, time)) 