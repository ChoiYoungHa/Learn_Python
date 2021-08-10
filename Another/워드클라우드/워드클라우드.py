text = "'한국폴리텍대학 서울강서캠퍼스(학장 노정진)는 데이터분석과 2학년 김한결, 황윤영, 홍두표 학생과 1학년 김도우 학생이 한이음 공모전에서 장려상을 받아 세종대학교에서 개최된 소프트웨어(SW) " \
       "인재페스티벌에 초청받았다고 10일 밝혔다. " \
       "과학기술정보통신부가 주최한 SW 인재페스티벌은 한이음 공모전 수상작에 대한 시상식이 진행됐다." \
       "이번에 수상한 작품은 빅데이터 분석을 활용한 음성 인식 스피치 교정 애플리케이션으로 최근 블라인드 채용으로 인해 면접에 대한 중요성이 강조되면서, 면접 교육을 위한 수강료 등 다양한 비용을 " \
       "감소시키기 위해 "


print(text)

from wordcloud import WordCloud, STOPWORDS
from tkinter import *

import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)
stopwords.add("위해")
stopwords.add("받아")
stopwords.add("분석을")

myWC = WordCloud(font_path="font/HMFMOLD.TTF", stopwords=stopwords, background_color="white").generate(text)

plt.figure(figsize=(5, 5))

plt.imshow(myWC, interpolation="lanczos")

plt.axis('off')

plt.show()

