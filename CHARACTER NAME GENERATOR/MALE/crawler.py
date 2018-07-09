# Import the libraries
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Scrape names from webpage
names = []
for i in range(1, 5):    
    link = "http://www.momjunction.com/baby-names/boy/starting-with-Z/page/" + str(i) + "/"
    req = Request(link, headers={"User-Agent": "Mozilla/5.0"})
    html = urlopen(req)
    bsObj = BeautifulSoup(html.read(), "html.parser", from_encoding="iso-8859-1")
    table_item = bsObj.find_all('td')
    for item in table_item:
        if "href" in str(item) and "void" not in str(item):
            names.append(str(item))
    print(str(i) + " scraped!")

# Save to file
file = open("Z-boy.txt", "w", encoding="utf-8")
for name in names:
    name = name.split("/\">")[1]
    name = name.split("</")[0]
    name = name.replace(" ", "")
    file.write(name + "\n")
file.close()