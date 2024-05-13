#整个请求中的常用的get post;利用post去抓取一些数据，返回百度翻译的数据;补充:关于get的params和close,get:参数拼接在url;思维探索，做自己的翻译器
import requests
import re
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
# proxies = {
#     'http':'http://127.0.0.1:9413',
#     'https':'https://127.0.0.1:9413'
# }

def create_pdf(text_list, output_filename):
    # 创建PDF文件
    c = canvas.Canvas(output_filename)
    # 设置页面大小
    c.setPageSize((600, 800))  # 设置页面宽度为600，高度为800
     # 指定使用的字体和字体大小
    font_name = "simsun"
    font_size = 12
    pdfmetrics.registerFont(TTFont(font_name, "C:\Windows\\Fonts\simsun.ttc"))
    # 设置字体
    c.setFont(font_name, font_size)
    # 设置起始纵坐标
    y = 780  # 起始纵坐标
    # 逐行写入文本内容
    for text in text_list:
        # 检查文本长度是否超出页面宽度
        if c.stringWidth(text, font_name, font_size) > 600:  # 如果文本长度超出页面宽度，可以进行处理
            # 可以进行文本分割或调整字体大小等操作来适应页面宽度
            pass 
        c.drawString(100, y, text)
        y -= 20  # 调整纵坐标，使文本不重叠
    c.save()
cookies = {
    'appmsg_token': '1259_1aLuigL6G0o0OkhPQy1DdFGLPviUZmxiGXuWr-Y6OFsDIAs2r2uEb_nbWFDNcAh6NLLjnCF03h8P2Az8',
    'rewardsn': '',
    'wxtokenkey': '777',
    'wxuin': '4120639646',
    'devicetype': 'Windows11x64',
    'version': '6309092b',
    'lang': 'zh_CN',
    'pass_ticket': 'zCYYqsYKm38DC4sRi5mUGCQJPzEXGKchN8Lf9eJtLFUnafavgewjzjA9UBzctr6LLaEmDUlfo2Qg5zml8pTAlw==',
    'wap_sid2': 'CJ7x76wPEooBeV9ITUo4Ry1USEU5My1Za1BMdlM0TWg1alhHRHNUN2pQbmlqa3k3M3ZKbm5ubTNvVGtjLW56X3BIa0pEazBDNGNPTm1ycGdJOHg1MFZtR1M2YkQyWWFILXdXTmRTNS1YWjNPODd5b2VNc3FZSWgwZFVFdnNEUXpreWFFUC1NNmZXTjlNa1NBQUF+MJXKla8GOA1AAQ==',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/8555 Flue',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'max-age=0',
    'x-wechat-key': 'de1cd1cd954fde5d49561b0f1b4b616b2408a2c8bfc16beb938c60b68376dd45a4d125112821fc94a333b524cef5e8aaa7ed2d81fd2e499220cad7f30825ddf3a2b11d0b14dd3b459c9c47e4f08b87340f797385e56dc3ed0ad8cce781763f1c200e8ec7006a40915bbc24a80504e01ae5e7f300775bc99d9a5e5fa16682d940',
    'x-wechat-uin': 'NDEyMDYzOTY0Ng%3D%3D',
    'exportkey': 'n_ChQIAhIQdvLrKeBJEsui3fDodDFThRLgAQIE97dBBAEAAAAAACiCFYZ5fGkAAAAOpnltbLcz9gKNyK89dVj0DyunPN8bSo9JpibufuXBQZfBo1T8cLidMYw%2F4GNeSA9YfxzD41%2F0BfwdaRZazJrIFO%2F79E9KOlBrO3RHhj5B81LB14g4i7CRoXGd%2BEcNMjjKIsS%2Bw2mCJIQWSeRj1DKhjPBkIBeRmAjnCxLqtKGQsimUUosMEPZLO5ObSHhATV0Fv%2BhPl3m3FGI%2BnVHQKpO%2Bfz17tHg5W0coIcc%2FVV0QW2Wa94P9subLJrhTr5IwuoUgC4uM3qtnBMzy',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'appmsg_token=1259_1aLuigL6G0o0OkhPQy1DdFGLPviUZmxiGXuWr-Y6OFsDIAs2r2uEb_nbWFDNcAh6NLLjnCF03h8P2Az8; rewardsn=; wxtokenkey=777; wxuin=4120639646; devicetype=Windows11x64; version=6309092b; lang=zh_CN; pass_ticket=zCYYqsYKm38DC4sRi5mUGCQJPzEXGKchN8Lf9eJtLFUnafavgewjzjA9UBzctr6LLaEmDUlfo2Qg5zml8pTAlw==; wap_sid2=CJ7x76wPEooBeV9ITUo4Ry1USEU5My1Za1BMdlM0TWg1alhHRHNUN2pQbmlqa3k3M3ZKbm5ubTNvVGtjLW56X3BIa0pEazBDNGNPTm1ycGdJOHg1MFZtR1M2YkQyWWFILXdXTmRTNS1YWjNPODd5b2VNc3FZSWgwZFVFdnNEUXpreWFFUC1NNmZXTjlNa1NBQUF+MJXKla8GOA1AAQ==',
}

url = 'https://mp.weixin.qq.com/s?__biz=MzA3MDI1OTMxOQ==&mid=2650278765&idx=1&sn=3f443cf039f13575829889439236428a&chksm=860318d5e41cdc2e2c612bd20886f6b66dd9ae2f92d0beb0fbe5c005a682b4390e0d2b06933f&scene=27&key=de1cd1cd954fde5d64f08d841ae6aa1198a49e7f793088b9c7b902fc29d8f3996a537a52cc43678b3327608d2f5a116f9469a31ea3c749b6f0e624d0d291b0ed6ab3ada12832ff15dab7c5ec1752cac37729c5373b7f7eaf7e80d605e5d97e4989308a817c6871ca3595b365ea857dd68947b29b3847f374d187e9fb9e0e2e74&ascene=0&uin=NDEyMDYzOTY0Ng%3D%3D&devicetype=Windows+11+x64&version=6309092b&lang=zh_CN&countrycode=CN&exportkey=n_ChQIAhIQV8UM%2BuxqKaHfxPGOGsfKvBLUAQIE97dBBAEAAAAAAIYmFw%2BYJEYAAAAOpnltbLcz9gKNyK89dVj03OWSu5wBZ5OxzRNYFXBRgZ4iHUkMMqrA%2BrItQDODfoi1gmXw4QSHj7apdF5UNLf44vjVyNtWM9W5NNTQSdmWfcyq9qVeaDAs0goToHJt2ZjOHlDrPvOdJ89MABFvm1%2FILcs8DS5IHhQBgtd2DwCrLKY6ejwW4LDX2If69wlBYFYZiuSiP4swGbMt46Vv2hDn%2BSwyYNCwZKLkiC6BiohWUtMFLSNT94QdWXRyRQ2%2B&acctmode=0&pass_ticket=DV3CnTnggIc%2B%2BhyxmabyFrDjZ0r7hUCe6c72XB%2F%2F4hRlMBo%2B0PBw8u8Qk8HWayYS0%2Bs4DTNEXLpThxjpLnEL2Q%3D%3D&wx_header=1'
#response = requests.get(url, cookies=cookies, headers=headers,proxies=proxies,verify=False)
response = requests.get(url, cookies=cookies, headers=headers)
html_data = response.text

# html_data是包含HTML内容的变量
soup = BeautifulSoup(html_data, 'html.parser')
# 查找所有带有<span>标签的内容
span_tags = soup.find_all('span')
# 提取所有<span>标签内的文本内容
text_list = [tag.get_text() for tag in span_tags]
# 指定输出的PDF文件名
output_filename = "resourcecode/pachong_information/original_data/output.pdf"
# 创建PDF文件并保存文本内容
create_pdf(text_list, output_filename)

if __name__ == "__main__":
    pass