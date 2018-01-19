from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


# 原型
# html = urlopen("https://baike.baidu.com/item/%E5%87%AF%E6%96%87%C2%B7%E8%B4%9D%E8%82%AF/2728128?fr=aladdin")
# bsObj = BeautifulSoup(html)
#
# # myImgTag.attrs["src"] 返回标签属性的内容
# for link in bsObj.find("div", {"class": "body-wrapper feature feature_small starSmall"}). findAll("a",href=re.compile("^(/item/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print("https://baike.baidu.com"+link.attrs['href'])

def get_link(url, tag_name, tag_attribute, tag_property, similarity, front_url):
    pages = set()
    try:
        html= urlopen(url)
    except HTTPError as e:
        return None
    try:
        obj = BeautifulSoup(html)
        outcome = obj.find(tag_name,{tag_attribute : tag_property}).findAll("a",href=re.compile("^(/"+similarity+"/)((?!:).)*$"))
        for link in outcome:
            if 'href' in link.attrs:
                # 当遇到新的页面时
                if link.attrs['href'] not in pages:
                    pages.add(link.attrs['href'])
                    print(front_url + link.attrs['href'])
        # 统计链接数量
        print(len(pages))
    except ArithmeticError as e:
        return None

# 例子
if __name__ == "__main__":
    get_link("https://baike.baidu.com/item/%E5%87%AF%E6%96%87%C2%B7%E8%B4%9D%E8%82%AF/2728128?fr=aladdin",
            "div","class","body-wrapper feature feature_small starSmall","item","https://baike.baidu.com")
