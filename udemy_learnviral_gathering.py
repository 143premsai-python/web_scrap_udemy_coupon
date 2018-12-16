import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from contextlib import closing
from datetime import datetime
start = datetime.now()
url = 'https://udemycoupon.learnviral.com'
res  = requests.get(url)
soup = BeautifulSoup(res.content,'html.parser')
price = soup.find_all('a',attrs={'class':'coupon-code-link btn promotion'})
for i in range(2,10):
    res  = requests.get(url+'/page/{}/'.format(i))
    soup = BeautifulSoup(res.content,'html.parser')
    price += soup.find_all('a',attrs={'class':'coupon-code-link btn promotion'})
li= set()
for i in price:
    li.add(i.get('href'))

import pandas as pd
writer = pd.ExcelWriter('udemy_learnviral.xlsx')
pd.DataFrame(list(li)).to_excel(writer,index=False)
writer.save()
writer.close()
print(datetime.now()-start)