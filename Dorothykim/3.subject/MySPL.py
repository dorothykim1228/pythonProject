import pymysql


#나의 db접속
# 접속
connection = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root',\
                             password ='1234', db ='students', charset ='utf8')
# 커서 가져오기 (연결할 db와 상호작용하기 위해 cursor 객체 생성필요)
cursor = connection.cursor()

# SQL문 만들기
sql = 'SELECT * FROM ai_class(db)'
cursor.execute(sql) # sql문 실행

result = cursor.fetchall()
for res in result:
    print(res)

connection.close()


# 서버 접속(다른 사람)

# 접속
connection = pymysql.connect(host = '192.168.0.62', port = 3306, user = 'root',\
                             password ='0000', db ='jochanigdb', charset ='utf8')

# 커서 가져오기 (연결할 db와 상호작용하기 위해 cursor 객체 생성필요)
cursor = connection.cursor()

# SQL문 만들기
sql = 'SELECT * FROM ai_class(db)'
cursor.execute(sql) # sql문 실행

result = cursor.fetchall()
for res in result:
    print(res)

connection.close()

#개체 생성(비번 생략 가능)

create user '상대방 아이디'@'상대방 ip' identified by '상대방 패스워드'
create user 'user명'@'host명' identified by '비밀번호'

#if 상대방 = 나:
#   상대방 ip 대신 localhost

#계정 삭제
drop user '상대방 아이디'@'상대방ip'
drop user 'user명'@'host명'

#데이터베이스 모든 권한 부여(비번 생략 가능)

GRANT ALL PRIVILEGES ON *.* TO '상대방 아이디'@'상대방 ip' IDENTIFIED BY '상대방 패스워드';

GRANT ALL PRIVILEGES ON *.* TO '상대방 아이디'@'상대방 ip' IDENTIFIED BY '상대방 패스워드';

#데이터 베이스 모든 권한 회수
revoke all on 데이터베이스명 from 'user명'@'host명'

#추가권한만 부여
grint insert on 데이터베이스명 to 'user명'@'host명'

#특정 권한 주기(비번 생략가능)
GRANT SELECT, UPDATE, DELETE, INSERT ON *.* TO '유저명'@'%' IDENTIFIED BY '상대방 패스워드';
#SELECT(조회), DELETE(삭제), INSERT(추가), UPDATE(수정)


#조회 권한만 부여
grint select on 데이터베이스명 to 'user명'@'host명'

#수정 권한만 부여
grint update on 데이터베이스명 to 'user명'@'host명'

#삭제 권한만 부여
grint delete on 데이터베이스명 to 'user명'@'host명'

#추가 권한만 부여
grint delete on 데이터베이스명 to 'user명'@'host명'


#데이터베이스에 여러테이블 중 accont_info라는 테이블만 조회 권한 부여
grant select on 데이터베이스명.account_info to 'user명'@'host명'

#권한 적용(권한이 변경될때)
flush privileges;

#host에 접속 가능한 'user명'의 권한 확인
show grants for 'user명'@'host'

#허용한 ip보내기
DELETE FROM pymysql.user WHERE HOST ='%' AND USER='user명';