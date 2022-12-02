# orm
# peewee

from peewee import *

db = PostgresqlDatabase('student', host='localhost',
                        port=5432,
                        user='postgres',
                        password='postgres')


class StudentTable(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = CharField(max_length=100)
    gender = CharField(max_length=50)
    course = IntegerField()
    kpi = IntegerField(null=True)

    class Meta:
        database = db
        db_table = 'student_tb'


class Task(Model):
    title = CharField(max_length=100)
    description = TextField()

    class Meta:
        database = db
        db_table = 'task_tb'


class StudentTask(Model):
    student_id = ForeignKeyField(StudentTable)
    task_id = ForeignKeyField(Task)
    mark = IntegerField

    class Meta:
        database = db
        db_table = 'student_task_tb'


db.connect()
db.create_tables([StudentTable, Task, StudentTask])


# row = StudentTable.select().where(StudentTable.gender == "Male",
#                                   StudentTable.first_name.startswith('W'),
#                                   StudentTable.first_name.endswith('y'))
# for i in row:
#     print(i.first_name, 'gender is', i.gender)

student = StudentTable.get(StudentTable.id==3)
student.kpi = 200
student.save()
#student.delete_instance()
print(student.first_name, student.last_name, student.kpi)