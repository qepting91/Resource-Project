import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a request to the webpage containing the HTML code
url = "https://nvf.org/veteran-resources/"
page = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# Find all the anchor tags on the page
links = soup.find_all('a')

# Extract the href attribute from each link
results = []
for link in links:
    results.append(link.get('href'))
    
print(results)
