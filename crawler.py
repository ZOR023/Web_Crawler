import requests 
from bs4 import BeautifulSoup 
import csv

countries = []

urls = ["https://www.scrapethissite.com/pages/simple/"]

while len(urls) != 0:
  current_url = urls.pop()
  
  response = requests.get(current_url)
  soup = BeautifulSoup(response.content, "html.parser")

  link_elements = soup.select("a[href]")
  
  for link_element in link_elements:
    url = link_element['href']
    if "https://www.scrapethissite.com/pages/simple/" in url:
      urls.append(url)
  
  country = {}
  country["url"] = current_url
  country["country_name"] = soup.select_one(".country-name").text
  country["Capital"] = soup.select_one(".country-capital").text
  country["Population"] = soup.select_one(".country-population").text
  country["Area"] = soup.select_one(".country-area").text

  countries.append(country)
  
with open('countries.csv', 'w') as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=countries[0].keys())
  
  writer.writeheader
  for country in countries:
    writer.writerow(country)
  
  print(countries)
