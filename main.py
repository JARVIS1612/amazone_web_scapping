import time
from bs4 import BeautifulSoup as bs
import requests as req

response = req.get("https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1690038574&sprefix=ba%2Caps%2C283&ref=sr_pg_1", timeout=500)
main_page = response.text

if response.status_code != 200:
   raise Exception(f"Some Error occure status code: {response.status_code}")

soup_obj = bs(main_page, "html.parser")

last_page = soup_obj.find("span", {'class':"s-pagination-item s-pagination-disabled"})

print(response.status_code)

# rows = soup_obj.find_all(class_="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t3 puis-include-content-margin puis puis-v1fjs7xta7k9po25ifhz337rduq s-latency-cf-section s-card-border")

# for row in rows:
#    name = row.find("span", {'class': 'a-size-medium'}).text
#    price = row.find("span", {'class': 'a-offscreen'}).text
#    ratings = row.find("span", {'class':"a-icon-alt"}).text
#    num_ratings = row.find("span", {'class':"a-size-base s-underline-text"}).text
#    url = row.find("a", {'class': 'a-link-normal'}).get('href')
#    print(f"name: {name}")
#    print(f"price: {price}")
#    print(f"url: {url}")
#    print(f"ratings: {ratings}")
#    print(f"num_ratings: {num_ratings}")
#    print("*"*50)


for i in range(2, int(last_page.text)+1):
   time.sleep(10)
   response = req.get(f"https://www.amazon.in/s?k=bags&page={i}&crid=2M096C61O4MLT&qid=1690038574&sprefix=ba%2Caps%2C283&ref=sr_pg_{i}", timeout=500)
   if response.status_code != 200:
      raise Exception(f"Some Error occure status code: {response.status_code}")
   
   main_page = response.text
   soup_obj = bs(main_page, "html.parser")

   last_page = soup_obj.find("span", {'class':"s-pagination-item s-pagination-disabled"}).text
   rows = soup_obj.find_all(class_="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t3 puis-include-content-margin puis puis-v1fjs7xta7k9po25ifhz337rduq s-latency-cf-section s-card-border")

   for row in rows:
      name = row.find("span", {'class': 'a-size-medium'}).text
      price = row.find("span", {'class': 'a-offscreen'}).text
      ratings = row.find("span", {'class':"a-icon-alt"}).text
      num_ratings = row.find("span", {'class':"a-size-base s-underline-text"}).text
      url = row.find("a", {'class': 'a-link-normal'}).get('href')
      print(f"name: {name}")
      print(f"price: {price}")
      print(f"url: {url}")
      print(f"ratings: {ratings}")
      print(f"num_ratings: {num_ratings}")
      print("*"*50)