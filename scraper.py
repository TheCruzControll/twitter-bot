# -*- coding: utf-8 -*-
import bs4
import requests

i = 1
file = open("quotes.txt", "w")
while i < 30:
    website = "https://www.goodreads.com/quotes?page=" + str(i)

    res = requests.get(website)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    quoteNum = 0
    while quoteNum < 30:
        cssSelector = 'body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div.quotes > div:nth-of-type('+str(quoteNum)+') > div.quoteDetails > div.quoteText'
        elems = soup.select("div.quoteText")
        elems2 = soup.select("span.authorOrTitle")
        a = elems[quoteNum].text.strip().split('―')
        b = elems2[quoteNum].text.strip()
        quote = '"'+a[0].strip('\n “ ” ')+'"'
        author = b
        fullQuote = quote+" - "+author+'\n'
        if len(fullQuote)<280:
            try:
                file.write(fullQuote)
            except UnicodeEncodeError:
                break
        quoteNum+=1
    i+=1
file.close()