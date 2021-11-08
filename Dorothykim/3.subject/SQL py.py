import sqlite3

conn = sqlite3.connect("ex0819ver2.db", isolation_level= None) # autocommit //파일을 불러올때
conn.row_factory = sqlite3.Row #딕셔너리 결과조회
cur = conn.cursor()
input_name = 'AL'
    #input("검색할 이름을 입력해주세요\n")

cur.execute("SELECT * FROM EMP WHERE ENAME like '%{}%'".format(input_name))
#실핼할 sql 문 #execute 터미널 안에 입력한다고 생각하면됨, 테이블 생성 (터미널 역할)

result = cur.fetchall()
#dic_result = dict(result)
# print(type(dic_result))
# print(type(dic_result['ENAME']), dic_result['ENAME'],type(dic_result['SAL']),dic_result['SAL'])


#튜플로 이루어진 리스트 #조회한 결과에 한 ROW는 TUPLE이고 전체결과는 리스트이다.
#조회된 결과에 한 pow는 tuple이고 전체 결과는 리스트이다

for row in result:
    dic_result = dict(row)
    print(type(dic_result))
    print(dic_result['ENAME'])
    if dic_result['ENAME'] == "ALLEN":
        print("ALLEN이 맞습니다.")

