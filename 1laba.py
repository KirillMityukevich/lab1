import requests
import re
urls = ['http://www.mosigra.ru/']
mails =[]
startUrl = 'http://www.mosigra.ru/'
dp=0
def  pars (pageUrl):    
    global urls
    global dp
    global mails
    dp +=1
    response = requests.get(pageUrl)
    if response.status_code == 200: 
        result = re.findall('href="(.*?)"',response.text)
        result2 = re.findall (r"[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",response.text)
        urlsNew = list(set(result))
        mailsNew = list(set(result2))
        for mail in mailsNew:
            mails.append(mail)
        if len(urlsNew) >0:
            for url in urlsNew:
                if url.find('mail') !=-1:
                    url = url[7:]
                    if url not in urls :
                        urls.append(url)
                elif len(url)>0  and url[0]=='#':
                    url='http://www.mosigra.ru/'+url
                    if url not in urls :
                        urls.append(url)
                else:     
                    if url not in urls:
                        urls.append(url)
                        if url[:18]=='http://www.mosigra' and dp<=1 and url.find('mode')==-1:
                            pars (url)
                            dp -=1
pars (startUrl)
mails= set(mails)
for u in mails:
    print (u)

