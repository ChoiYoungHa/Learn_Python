import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

# 파싱할 데이터 위의 html 변수 , 데이터를파싱할 파서 html.parser
bs_obj = bs4.BeautifulSoup(html, "html.parser")

top_right = bs_obj.find("div", {"class": "theme_cont"})
one = top_right.find("div", {"class": "title_area"})
two = one.find("span", {"class": "blind"})

# 2021.08.08 기준 TOKYO 2020 데이터 추출
print(two.text)
