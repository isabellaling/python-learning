import requests
from bs4 import BeautifulSoup

res = requests.get('http://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1')

print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

trs = soup.select('#oTable > tbody tr')

print(len(trs))

for tr in trs:

    fc = tr.find('td', attrs={'class':'bzdm'}).string
    fn = str(tr.find('td', attrs={'class':'tol'}).find('nobr').contents[0].string).decode('utf-8')
    value = tr.find('td', attrs={'class':'dwjz black'}).string

    print(fc,fn,value)
