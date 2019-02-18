#https://www.imdb.com/title/tt0825232/reviews?ref_=tt_urv



import requests
from lxml import html
from bs4 import BeautifulSoup


from googletrans import Translator
translator = Translator()


#for i in range(800000,899999):
for i in range(800000,800010):
    link="https://www.imdb.com/title/tt"+str(i).zfill(7)+"/reviews?ref_=tt_urv"
    try:
        nam:str
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        for t in soup.findAll(itemprop="name"):
            for x in t.findAll(itemprop="url"):
                nam=x.get_text()
        for td in soup.findAll( class_="lister"):
            a=td.findAll(class_="text show-more__control")
            if a[0].get_text():
                print(nam,"\n\n")
                print(a[0].get_text(),"\n\n")
                text = translator.translate(a[0].get_text(), src='en', dest='bn')
                print(text.text,"\n\n")
    except:
        pass
