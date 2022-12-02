# psycopg2

import psycopg2
import random

conn = psycopg2.connect(database="student", host="localhost", port=5432, user="postgres", password="postgres")
cur = conn.cursor()
# cur.execute(
#     '''create table student_tb (
# 	    id INT,
# 	    first_name VARCHAR(50),
# 	    last_name VARCHAR(50),
# 	    email VARCHAR(50),
# 	    gender VARCHAR(50),
# 	    course INT
# );''')

with open('student_tb.sql', 'r') as f:
    data = f.read()
    cur.execute(f'''{data}''')

# cur.execute('''select id from student_tb;''')
# one_record = cur.fetchone()
# all_records = cur.fetchall()
# count = cur.rowcount
# print(count)
#print("success created!")
# for i in all_records:
#     cur.execute(f'''UPDATE student_tb SET kpi={random.randint(100, 150)} where id={i[0]}''')
# cur.execute('''select kpi from student_tb where kpi>130;''')
# kpi_130 = cur.rowcount
# cur.execute('''select first_name, last_name from student_tb where course=0 and gender='Male';''')
# all_students = cur.fetchall()
# cur.execute('''select id, first_name, kpi,  avg(kpi) from student_tb group by id, first_name, kpi order by id;''')
# avg = cur.fetchall()
# for i in avg:
#     print(i)

# print(kpi_130)
# print(all_students)
# print(avg)
conn.commit()
conn.close()
