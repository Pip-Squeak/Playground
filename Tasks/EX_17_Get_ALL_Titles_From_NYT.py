"""EX.17
Exercise:

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the
New York Times homepage.

Discussion:
- Libraries
- requests
- BeautifulSoup
"""
import requests
from bs4 import BeautifulSoup


url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

print("\n================================NYT-TITLES-OF-THE-DAY================================\n")

# looping titles by 'p class'
for titles in soup.find_all(class_="css-91bpc3"):
    print(f"\n{titles.get_text().strip()}\n")
