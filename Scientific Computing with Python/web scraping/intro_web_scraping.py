# Intro to web scraping.
# Using the Beatiful Soup 4, we get the html from an address and look for the 
# <a> tag link. The for loop retrieves all the links at the site's tags. 
# from Python for Everybody at freecodecamp.org
# 12/06/22
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
