from bs4 import BeautifulSoup
import requests, re 

r = requests.get('https://www.kohls.com/product/prd-3770046/mens-tek-gear-classic-fit-golf-polo.jsp?color=Dress%20Blues&prdPV=3').content
soup = BeautifulSoup(r, 'lxml')

tags = soup.findAll("div", {"class":re.compile('(pdp-title-container)')})
for h in tags:
    h1s = h.findAll("h1")
    for i in h1s:
        titles = i.findAll("h1",{"class":"product-title"})
        for t in titles:
            title = t.string
            prices = h.findAll("p",{"class":"pdpprice-row2"})
            for p in prices:
                price = p.string
                print("Item %s costs %s" % (title,price))

