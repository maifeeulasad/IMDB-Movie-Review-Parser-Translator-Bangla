#https://www.imdb.com/title/tt0825232/reviews?ref_=tt_urv

import requests
from lxml import html
from bs4 import BeautifulSoup
from googletrans import Translator
from gensim.summarization import summarize
import re

def cleanhtml_c_(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  if int(cleantext)>6:
      return "pos"
  else:
      return "neg"
    
translator = Translator()


#for i in range(800000,899999):
for i in range(800000,800009):
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
            rat = soup.findAll(class_="rating-other-user-rating")
            ratin:str
            for r in rat:
                ratin=r
                break
            rev_c:str
            rrr:str
            for xx in ratin:
                if len(xx)==1 and len(str(xx))>13 and len(str(xx))<16:
                    rev_c = cleanhtml_c_(str(xx))
               
            if a[0].get_text():
                print("-------------------------------------------------")
                print(rev_c)
                print(nam,"\n\n")
                texet=summarize(a[0].get_text())
                print(texet,"\n\n")
                text = translator.translate(texet, src='en', dest='bn')
                print(text.text,"\n\n")
            
    except:
        pass

