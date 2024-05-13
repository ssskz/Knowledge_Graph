import requests
from bs4 import BeautifulSoup

# 指定网址
url = "http://www.81.cn/"

# 发起GET请求并获取网页内容
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 搜索包含关键字"报告"的内容并提取前十条数据
reports = []
for link in soup.find_all('a'):
    if link.text and '报告' in link.text:
        reports.append(link['href'])
        if len(reports) == 10:
            break

# 打印前十条包含关键字"报告"的链接
for i, report in enumerate(reports):
    print(f"报告{i+1}: {report}")