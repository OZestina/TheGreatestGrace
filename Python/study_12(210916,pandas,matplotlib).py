import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
import requests
import pandas as pd
from bs4 import BeautifulSoup

##시각화
url = "https://movie.naver.com/movie/running/current.naver"
#result
result = requests.get(url)
#content
content = BeautifulSoup(result.content, "html.parser")
#dt_list
dt_list = content.findAll("dt",{"class":"tit"})
print(len(dt_list))
print(dt_list[0].find("a").text)


#top 10 title
title = []
for dt in range(10):
    title.append(dt_list[dt].find("a").text)

#score_list
score_list = content.select('dl.info_star dd div.star_t1 a span.num')
print(len(score_list))
#print(score_list)

#top 10 scores
scores = []
for score in range(10):
    scores.append(float(score_list[score].text))

#how to make panda DataFrame!
df = pd.DataFrame({"title":title, "rate":scores})

#2x2 matrix with column&row index
print(df)
#print(df[10:20])

#descripions (numbers)
result = df.describe()
#print(result)

print(df.head(3))   #0<= index <3
print(df.info())    #data type
print(df.index)     #index range => RangeIndex(start=0, stop=10, step=1)

print("movie titles")
print("===================")
print(df['title'])  #DataFrame에서 정해준 이름
print("===================")
print(df['rate'])  #DataFrame에서 정해준 이름
print(df.sort_values(by='rate', ascending=False))

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
plt.plot(df['title'],df['rate'])
plt.show()
