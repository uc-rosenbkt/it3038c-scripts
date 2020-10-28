from bs4 import BeautifulSoup
import requests, re 

r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone').content
soup = BeautifulSoup(r, 'lxml')

tags = soup.findAll("div", {"class":re.compile('(caption)')})
for h in tags:
    h4s = h.findAll("h4")
    for i in h4s:
        titles = i.findAll("a",{"class":"title"})
        for t in titles:
            title = t.string
            prices = h.findAll("h4",{"class":"pull-right price"})
            for p in prices:
                price = p.string
                print("Item %s costs %s" % (title,price))

