import requests
from bs4 import BeautifulSoup

#specify the websit url
url=input("Enter the website url:")

#send the request to the website
response=requests.get(url)

#parse html content
soup=BeautifulSoup(response.text,"html.parser")

#extract the page title
title=soup.title.text

print("Website Title:",title)
#extract all H1 headings
print("\nHeadings:")
for heading in soup.find_all("h1"):
    print(heading.text)
