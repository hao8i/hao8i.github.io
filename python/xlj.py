import csv, requests, re
from bs4 import BeautifulSoup

url = 'https://hao8i.github.io/dh123/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
articles = []
for myweb in soup.find_all(class_='myweb'):
    myweb_u = myweb.select('a')
    grp_title = myweb_u[0].get_text()
    myweb_site_align = myweb.select('.myweb_site_align')
    for article in myweb_site_align:
        print(article)
        u = article.select('a')
        print(str(u))
        tip = re.findall(r'(?<=title=").+?(?=")', str(u))[0]
        title = u[0].get_text()
        link = 'https://hao8i.github.io/' + re.findall(r'(?<=href=").+?(?=")', str(u))[0]
        articles.append([grp_title, title, link, tip])

with open(r'document\xlj.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['网站组标题', '网站标题', '网站地址', '网站提示'])
    for row in articles:
        writer.writerow(row)
