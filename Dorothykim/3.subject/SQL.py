import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

#여러개 한꺼번에 insert하는법 #튜플 사용
test_tuple =(
    (4, '효정','최효정','오마이걸','1994-07-28'),
    (5, '미미','김미현','오마이걸','1995-05-01'),
    (6, '유아','유시아','오마이걸','1994-08-18'),
)


#conn.execute('INSERT INTO employee_data(id INTEGER, name TEXT, nickname TEXT, department TEXT, employment_date TEXT)')


conn.executemany("INSERT INTO employee_data(id, name, nickname, department, employment_date) VALUES(?,?,?,?,?)", test_tuple )

#cur.execute("SELECT name, department FROM employee_data")
#sqloutput = cur.fetchall()
#rint(sqloutput)

conn.commit()
conn.close()
