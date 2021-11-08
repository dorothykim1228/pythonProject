# b = 1
#
# print(b)
z = '제주점'

a = [('제주점',1),('광주점',2),('서울점',3),('전주점',4),('순천점',5)]

b = list(map(lambda x : x[0], a))
print(b, type(b))
print(z, type(z))
#
# for row in a:
#     print(row)

# print(b[0])

if z in b:
    print(12312312312312312131223123123)

    # self.page1


# import pymysql
#
# # # 접속
# connection = pymysql.connect(host='192.168.0.54', port=3306, user='root', password='1234',\
#                              db='headquarter', charset='utf8')
# # 커서 가져오기(연결할 db와 상호작용하기 위해서 cursor 객채생성 필요)
# cursor = connection.cursor()
# #
# #sql문 만들기
# qy = """
# select bsname from dsinfo
# """
#
# #sql문 실행
# cursor.execute(qy)
#
# iy = cursor.fetchall()
# for row in iy:
#     print(row)

# qy = """
# select APPROVE from bsinfo where bsname = %s
# """
# # sql문 실행
#
# a = ('제주점')
# b = cursor.execute(qy, a)
# print(b)
#
# connection.close()
