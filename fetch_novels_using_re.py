import requests
import re

def getNextUrl(currentPageContent):
    nextUrl = 'Https:' + re.findall('<a id="j_chapterNext" href="(.*?)"', currentPageContent)[0]
    return nextUrl

def getPageContent(url):
    response = requests.get(url)
    results = re.findall('<p>(.*?)<', response.content.decode('utf-8'), re.S)
    return results


def getNextPage(index, currentPageContent):
    nextUrl = getNextUrl(currentPageContent)

    cts=getPageContent(nextUrl)

    results = '第' + str(index) + '章\n'
    results += '-------------------------------\n'

    for ct in cts:
        results = results + ct + '\n'

    return results

# 正文

res=requests.get('https://read.qidian.com/chapter/2R9G_ziBVg41/MyEcwtk5i8Iex0RJOkJclQ2');

paragraphs=re.findall('<p>(.*?)<', res.content.decode('utf-8'), re.S)

f=open('/Users/isabella/Desktop/index.txt','w+')

f.write('第1章\n')
f.write('-------------------------------\n')

for ct in paragraphs:
    f.write(ct+'\n')

nextUrl = getNextUrl(res.text)

for index in range(2,12):

    res = requests.get(nextUrl)
    paragraphs = re.findall('<p>(.*?)<', res.content.decode('utf-8'), re.S)

    nextUrl = getNextUrl(res.text)

    results = '第' + str(index) + '章\n'
    results += '-------------------------------\n'

    for p in paragraphs:
        results = results + p + '\n'

    f.write(results)


f.close()



