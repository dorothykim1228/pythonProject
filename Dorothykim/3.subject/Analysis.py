import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#파일 경로
file_path1 = 'chipotle.tsv'
file_path2 ='drinks.csv'

# #판다스의 데이터 프레임을 생성
#
# names = ['Bob', 'Jessica', 'Mary', 'John','Mel']
# births = [968,155,74,578,973]
# custom = [1,5,25,13,23232]
# #
# BabyDataSet = list(zip(names,births))
# df = pd.DataFrame(data = BabyDataSet, columns = ['Names','Births'])
# #
# y = df['Births']
# x = df['Names']
#
# # #막대 그래프를 출력
# plt.bar(x,y)  # 막대그래프 객체 생성
# plt.xlabel('peter') # x축 제목
# plt.ylabel('births') # y축 제목
# plt.title('bar plot') # 그래프 제목
# plt.show() # 그래프 출력
#
# #
# #데이터 프레임의 상단부분을 출력하기
#
# print(df.head())
# # print(df.dtypes)
#
#
# # 산점도 출력하기
# # 랜덤 추출 시드 고정
# np.random.seed(19920613)
#
# #산점도 데이터 생성
# x = np.arange(0.0, 100.0, 5.0)
# y = (x * 1.5) + np.random.rand(20) * 50
#
#산점도 데이터 출력
#산점도 그래프 세팅, c의 의미는 색깔, b의 의미는 blue의 약자
#
# plt.scatter(x, y, c = "g", alpha = 0.5, label = "scatter point")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend(loc ='upper left') #그래프 세틍
# plt.title('Scatter plot') #그래프 이름
# plt.show()
#
#
# #위키도키 예제 하기
# # 200ms 간격으로 균일하게 샘플된 시간
# t = np.arange(0., 5., 0.2)
#
# # 빨간 대쉬, 파란 사각형, 녹색 삼각형
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
#
#
#
# #배열 자동 생성
# arr1 =np.arange(15).reshape(3,5)
# print(arr1)
# #
# #배열의 요소 타입 확인
# # print(arr1.dtype)
# #
# # arr3 = np.zeros((3,4))
# print(arr3)
#
# arr4 = np.array([[1,2,3],[4,5,6]], dtype= np.float64)
# arr5 = np.array([[7,8,9],[10,11,12]], dtype= np.float64)
#
# # 사칙 연산 출력
# print("arr4 + arr5 = ")
# print(arr4 + arr5, "\n")
# print("arr4 - arr5 = ")
# print(arr4 - arr5, "\n")
# print("arr4 * arr5 = ")
# print(arr4 * arr5, "\n")
# print("arr4 / arr5 = ")
# print(arr4 / arr5, "\n")
#
# # 계산하기
#
# a = [[1,2,3],[4,5,6]]
# b = [[7,8,9],[10,11,12]]
# c = []
#
# for i in range(len(a)):
#     d= []
#     for y in range(len(a[0])):
#         d.append(a[i][y]+b[i][y])
#         c.append(d)
# print(c)
#
# # 함수 안쓰고 2차원 list 더하기
# arr1 = [[1,2,3,],[4,5,6]]
# arr2 = [[4,5,6,],[7,8,9]]
# for i in range(len(arr1)):
#     for y in range(len(arr1[i])):
#         arr1[i][y] += arr2[i][y]
# print(arr1)



#chipotle 주문 데이터 분석하기

# file_path = 'chipotle.tsv'
# #read_cvs()함수로 데이터를 프레임 형태로 불러옴
# chipo = pd.read_csv(file_path,sep = '\t')
#
# print(chipo.shape)
# print("--------------------------------")
# print(chipo.info())
#
#chipotle 데이터셋의 행과 열, 데이터 확인하기
#chipo 데이터 프레임에서 순서대로 10개의 데이터 보여줌
#
# print(chipo.head(10))
#
# print(chipo.columns)
# print("------------------------------")
# print(chipo.index)
#
# #9/8
#
# chipo['order_id'] = chipo['order_id'].astype(str)
# #기초 통계란 출력하기
# print(chipo.describe())
#
# # 범주형 피처의 개수 출력하기, unique - 중복x, len으로 길이(개수)
#select count(order_id) from chipo - #쿼리인 경우
# print(len(chipo['order_id'].unique()))
# print(chipo['item_name'].unique())
#
# # 가장 많이 주문한 아이템 top 10 출력하기
# Item_count = chipo['item_name'].value_counts()[:10]
#print(type(Item_count))
#
#for idx, (val,cnt) in enumerate(Item_count.iteritems(),1):
#     print("TOP", idx, ":", val, cnt)
    # print(type(idx))
    # print(type(val))
    # print(type(cnt))


#스타벅스 같은 데이터를 만들었을때, 공공데이터 csv
#ui 반영하면 top 10 시각화해서 보여줄수 있음
#groupby로 아이템별로 묶고, 주문수량을 count로 구한다
#주문된 기록을 통해 메뉴별 개수를 구할수 있다

# 아이템별 주문 개수와 총량
#order_count = chipo.groupby(['item_name'])['order_id'].count() #주문개수
# print(order_count[:10])

# 아이템별 주문 개수 출력

#order_count = chipo.groupby('item_name')['order_id'].count()
#print(order_count[:10])

#아이템별 주문 총량
#groupby로 아이템별로 묶고, 주문수량을 sum로 구한다
#item_quantity = chipo.groupby('item_name')['quantity'].sum() #주문수량
# print(item_quantity)


# 시각화(p.56)
#y값(order_cnt)에 주문 총량[item_quantity.values.tolist()]을 넣는다

#import matplotlib.pyplot as plt
#import nump as np
#
# item_name_list = item_quantity.index.tolist()
# x_pos =np.arange(len(item_name_list))
# order_cnt = item_quantity.values.tolist()
#
# plt.bar(x_pos, order_cnt, align='center') #그래프 세팅
# plt.ylabel('ordered_item_count') #y라벨 이름
# plt.title('Distribution of all orderd item') #그래프 이름
#
# plt.show()

# 데이터 전처리: Raw Data가 있다면 수집과 쉽게 보기 위해 하는 작업

# # 처리 후 $표시 제거 후 다시 item_price에 저장(float형태,첫번쨰부터 가져옴)
# chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
# print(chipo.describe())
#
# # 주문당 평균 계산 금액출력하기
# # 주문당(order_id로 groupby) 금액의 총합의 평균(sum().mean())
#averagePrice =chipo.groupby('order_id')['item_price'].sum().mean()
# print(averagePrice)
#
# # 한 주문에 10달러 이상 지불한 주문 번호 (id) 출력
# chipoo_orderid_group = chipo.groupby('order_id').sum()
# results = chipoo_orderid_group[chipoo_orderid_group.item_price >= 10]
# print(results[:10])
# print(results.index.values)

# 각 아이템의 가격 구하기
# 주문번호에서 수량이 하나인 주문은 주문가격이 아이템의 가격



# chipo_one_item = chipo[chipo.quantity == 1] # 수량이 하나인 order 구하기
# price_per_item = chipo_one_item.groupby('item_name').min() # 해당 item_name 기준으로 최저값 구하기
# results = price_per_item.sort_values(by = "item_price", ascending= False)[:10] # 내림차순으로 정렬(ascending(오름차순)= False)
# print(results)

#가장 비싼 주문에서 총 몇개 팔렸는지 구하기
#order id로 묶은 후 가격을 더하고 가격별로 내림차순 정렬
#chipo.groupby('order_id').sum().sort_values(by='item_price', ascending = False)[:5]
#print(results)

# Veggie Salad Bowl이 몇 번 주문되었는지 구하기
# chipo_salad = chipo[chipo['item_name'] == "Veggie Salad Bowl"]
# #중복제거(duplicates)
# chipo_salad = chipo_salad.drop_duplicates(['item_name','order_id'])
# pd.set_option('display.max_columns', 4)
#
# print(len(chipo_salad))
# print(chipo_salad.head(5))



#
#
# chipo_chicken = chipo[chipo['item_name'] == 'Chicken Bowl']
# #같은 주문번호로 묶고 더하고 chicken bowl의 수량을 구함
# chipo_chicken_ordersum = chipo_chicken.groupby('order_id').sum()['quantity']


#Chicked bowl 2개 이상을 주문한 주문 횟수 구하기
# chipo_chicken_result = chipo_chicken_ordersum[chipo_chicken_ordersum >= 2]


# print(len(chipo_chicken_result))
# print(chipo_chicken_result.head(5))
#
# #교과서
# chipo_chicken = chipo[chipo['item_name'] == 'Chicken Bowl']
# chipo_chicken_result = chipo_chicken[chipo_chicken['quantity'] >= 2]
# print(chipo_chicken_result.shape[0])

# 국가별 음주 데이터 분석하기

drinks =pd.read_csv(file_path2)

print(drinks.info)
print(drinks.head(10))

print(drinks.describe())

# beer 소비량과 와인소비량의 상관 계수 계산
corr = drinks[['beer_servings','spirit_servings', 'wine_servings','total_litres_of_pure_alcohol']].corr(method= 'pearson')
print(corr)

cols_view = ['beer','spirit','wine','alcohol'] #그래프 출력을 위한 cols 이름 축약
sns.set(font_scale = 1.5)
hm = sns.heatmap(corr.values,
        cbar = True,
        annot = True,
        square = True,
        fmt ='.2f',
        annot_kws = {'size': 15},
        yticklabels = cols_view,
        xticklabels = cols_view)

plt.tight_layout() # tight_layout()메소드는 서브 플롯간에 올바른 간격을 자동으로 유지
plt.show()

#시각화 라이브러리 이용한 피처 간의 산점도 그래프 출력

sns.set(style = 'whitegrid', context = 'notebook')
sns.pairplot(drinks[['beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol']],height = 2.5)
plt.show()