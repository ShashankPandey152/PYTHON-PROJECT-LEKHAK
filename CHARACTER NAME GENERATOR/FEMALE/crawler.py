# Import the libraries
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Scrape names from webpage
names = []
i = 1
flag = 0
while(True):   
    link = "http://www.momjunction.com/baby-names/girl/starting-with-Z/page/" + str(i) + "/"
    req = Request(link, headers={"User-Agent": "Mozilla/5.0"})
    html = urlopen(req)
    bsObj = BeautifulSoup(html.read(), "html.parser", from_encoding="iso-8859-1")
    table_item = bsObj.find_all('td')
    for item in table_item:
        if "NO DATA" in str(item):
            flag = 1
            break
        if "href" in str(item) and "void" not in str(item):
            names.append(str(item))
    if(flag == 1):
        break
    print(str(i) + " scraped!")
    i += 1

# Save to file
file = open("Z-girl.txt", "w", encoding="utf-8")
for name in names:
    name = name.split("/\">")[1]
    name = name.split("</")[0]
    name = name.replace(" ", "")
    file.write(name + "\n")
file.close()
