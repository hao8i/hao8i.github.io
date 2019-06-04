#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 导入外部依赖软件包
import csv, requests, re
from bs4 import BeautifulSoup

# 设置网页路径
url = 'https://hao8i.github.io/dh123/'
#url = 'http://localhost:8280/xlj2019/dh123/'
# 抓取网页
html = requests.get(url).text
# 分析网页
soup = BeautifulSoup(html, 'html.parser')
# 保存结果数组变量
articles = []
# 抽取所有class 属性为myweb的网页元素
for myweb in soup.find_all(class_='myweb'):
    # 抽取所有<a>元素
    myweb_u = myweb.select('a')
	# 获得网站组标题
    grp_title = myweb_u[0].get_text()
	# 选择所有class 属性为myweb_site_align的网页元素
    myweb_site_align = myweb.select('.myweb_site_align')
    for article in myweb_site_align:
        print(article)
		# 抽取所有<a>元素
        u = article.select('a')
        print(str(u))
		# 通过正则表达式获得网站提示信息
        tip = re.findall(r'(?<=title=").+?(?=")', str(u))[0]
		# 获得网站标题
        title = u[0].get_text()
		# 通过正则表达式获得网站链接地址
        link = re.findall(r'(?<=href=").+?(?=")', str(u))[0]
		# 将数据保存到数组
        articles.append([grp_title, title, link, tip])

with open(r'xlj.csv', 'w', encoding = 'utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['网站组标题', '网站标题', '网站地址', '网站提示'])
    for row in articles:
        writer.writerow(row)
