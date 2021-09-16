#지상파tv 시청률 top10 프로그램과 그 시청률을 추출해보자
#url: https://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=1_1&area=01

import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
import requests
import pandas as pd
from bs4 import BeautifulSoup

#[top10 리스트 추출]
url = "https://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=1_1&area=01"
#result
result = requests.get(url)
#content
content = BeautifulSoup(result.content, "html.parser")

#title_list
title_list = content.findAll("td",{"class":"tb_txt"})
print(len(title_list))
# print(title_list[0].text)

#top 10 title
titles = []
for i in range(10):
    titles.append(title_list[i].text.strip())
    # print(title_list[i].text)

#rating_list
rating_list = content.findAll("td",{"class":"percent"})
# print(len(rating_list))

#top 10 ratings
ratings = []
for i in range(10):
    ratings.append(float(rating_list[i].text))
    # print(float(rating_list[i].text))


df = pd.DataFrame({"title":titles, "rating":ratings})
# print(df)

print("movie titles")
print("===================")
print(df['title'])  #DataFrame에서 정해준 이름
print("===================")
print(df['rating'])  #DataFrame에서 정해준 이름

#마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False


if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

plt.figure()
plt.xlabel('title')
plt.ylabel('rate')
plt.plot(df['title'],df['rating'])
plt.show()
