"""
1、查询所有的课程的名称以及对应的任课老师姓名
2、查询平均成绩大于八十分的同学的姓名和平均成绩
3、查询没有报李平老师课的学生姓名
4、查询没有同时选修物理课程和体育课程的学生姓名
5、查询挂科超过两门(包括两门)的学生姓名和班级
"""

import pymysql

conn = pymysql.connect(
    user='root',
    passwd='xjyaws',
    host='127.0.0.1',
    port=3306,
    database='day41',
    charset='utf8'
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# ex1
sql1 = 'select course.cname, teacher.tname from course inner join teacher on course.teacher_id = teacher.tid'
cursor.execute(sql1)
ans1 = cursor.fetchall()

# ex2
sql2 = 'select student.sname, t1.avg_score from student ' \
       'inner join ' \
       '(select student_id, avg(num) as avg_score from score group by student_id) as t1 ' \
       'on student.sid = t1.student_id ' \
       'where t1.avg_score >=80'
cursor.execute(sql2)
ans2 = cursor.fetchall()

# ex3
sql3 = 'select sname from student where sname not in (select raw.sname from ' \
       '(select t1.sname as sname, t2.tid as tid from ' \
       '(select score.sid as sid, student.sname as sname from score ' \
       'inner join ' \
       'student on score.student_id = student.sid) as t1 ' \
       'inner join ' \
       '(select score.sid as sid, course.teacher_id as tid from score ' \
       'inner join ' \
       'course on score.course_id = course.cid) as t2 ' \
       'on t1.sid = t2.sid) as raw ' \
       'inner join ' \
       'teacher ' \
       'on raw.tid = teacher.tid ' \
       'where teacher.tname = "李平老师")'
cursor.execute(sql3)
ans3 = cursor.fetchall()

# ex4
sql4 = 'select sname from student where sname not in ' \
       '(select t1.sname from ' \
       '(select score.sid as sid, student.sname as sname from score ' \
       'inner join ' \
       'student on score.student_id = student.sid) as t1 ' \
       'inner join ' \
       '(select score.sid as sid, course.cname as cname from score ' \
       'inner join ' \
       'course on score.course_id = course.cid) as t2 ' \
       'on t1.sid = t2.sid ' \
       'where t2.cname = "物理") ' \
       'or sname not in ' \
       '(select t1.sname from ' \
       '(select score.sid as sid, student.sname as sname from score ' \
       'inner join ' \
       'student on score.student_id = student.sid) as t1 ' \
       'inner join ' \
       '(select score.sid as sid, course.cname as cname from score ' \
       'inner join ' \
       'course on score.course_id = course.cid) as t2 ' \
       'on t1.sid = t2.sid ' \
       'where t2.cname = "体育")'
cursor.execute(sql4)
ans4 = cursor.fetchall()

# ex5
sql5 = 'select t2.sname, class.caption from' \
       '(select student.class_id as id, student.sname as sname from ' \
       '(select student_id from score where num < 60 group by student_id having count(num) >= 2) as t1 ' \
       'inner join ' \
       'student ' \
       'on t1.student_id = student.sid) as t2 ' \
       'inner join ' \
       'class ' \
       'on t2.id = class.cid'
cursor.execute(sql5)
ans5 = cursor.fetchall()

# ans
print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
