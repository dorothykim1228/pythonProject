# from bs4 import BeautifulSoup
# from pprint import pprint
# from urllib.request import urlretrieve #추가
# import requests, re
#
# # 웹 페이지를 열고  소스코드를 읽어오는 작업
#
# html = requests.get("https://comic.naver.com/webtoon/weekday")
# soup = BeautifulSoup(html.text, 'html.parser')
# html.close()
#
#
#
#
# #요일별 웹툰 영역 추출하기
# #bs4 html tag기반으로 찾는 함수
# data1_list =soup.findAll('div',{'class': 'col_inner'})
# # pprint(data1)
#
# li_list = []
#
# for data1 in data1_list:
#     #제목+썸내일 영역 추출
#     li_list.extend(data1.findAll('li')) #해당부분을 찾아 li_list와 병합
# # pprint(li_list)
#
# #각각 썸네일과 제목 추출하기
# for li in li_list:
#     img = li.find('img')
#     title = img['title']
#     img_src = img['src']
#     # print(title,img_src)
#     title = re.sub('[^0-9a-zA-Zㄱ-힗]','',title)
#     #정규식 파일, 이미지 파싱할떄 특정한 이름을 가진 애들만 가져오고 싶으면 정규식 가지고 id,pw만들때 이상한거 못넣게 함
#     #해당 영역의 글자가 아닌 것은 ''로 치환한다.
#     urlretrieve(img_src, './images/'+title+'.jpg')
#     #주소, 파일경로+파일명+확장자
#
#
#
# #제목 포함영역 추출하기
# data2 = data1.findAll('a',{'class':'title'})
# # pprint(data2)
#
# title_list = []
# for t in data2:
#     title_list.append(t.text)
#
# pprint(title_list)

import dload
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

#실행할 크롬 드라이버 경로
driver = webdriver.Chrome('chromedriver')

#파싱할 Url
baseUrl = 'https://pokemonkorea.co.kr/pokedex'


#driver로 url open
driver.get(baseUrl)

time.sleep(3) # 5초동안 페이지 로딩 기다리기
req = driver.page_source
soup = bs(req, "html.parser")


imgs = []
for i in range(1,10):
    #css 속상기반으로 찾는 함수 select(모두), select_one(한개만)
    img = soup.select('#\#pokedex_1 > a > div.img > div > img'.format(i))
    imgs.append(img)

i = 1
for img in imgs:
    for img2 in img:
        image_src = img2['src']
        dload.save(image_src, f'image/{i}.jpg')
        i += 1

driver.quit()