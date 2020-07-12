from django.db import models

# Create your models here.

#学生表
class Stu(models.Model):
    s_name = models.CharField('学生姓名',max_length=64,null=False,help_text='学生姓名')
    s_sex = models.CharField("性别",max_length=1,choices=(
        (0,'男'),
        (1,'女')
    ),help_text='性别：0-男；1-女')
    s_age = models.PositiveIntegerField('年龄',null=False,default=0,help_text='年龄')
    s_dept = models.CharField("专业",max_length=64,null=False,help_text="专业")
    s_id = models.OneToOneField(to='StudentInfo',to_field="id",on_delete=models.CASCADE,db_column='s_id',related_name="stu_student_info")
    course = models.ManyToManyField(to="Course",db_table="stu_course",related_name="course_stu")

    class Meta:
        db_table='stu'

#学生信息表
class StudentInfo(models.Model):
    s_card = models.CharField("身份证号",max_length=18,null=False,unique=True)
    s_phone = models.CharField(max_length=11,null=False,unique=True,help_text="手机号")
    s_addr = models.CharField("家庭住址",max_length=128,help_text="家庭住址")

    class Meta:
        db_table="student_info"

#课程表
class Course(models.Model):
    c_name = models.CharField('课程名',max_length=64,null=False,help_text="课程名")
    t_id = models.ForeignKey(to="Teacher",to_field="id",on_delete=models.CASCADE,related_name='teacher_course',db_column='t_id',help_text="老师编号")
    class Meta:
        db_table="course"

#成绩表
class Score(models.Model):
    s_id = models.ForeignKey(to="Stu", to_field="id", on_delete=models.CASCADE, related_name='stu_score',
                             db_column='s_id', help_text="学生编号")
    c_id = models.ForeignKey(to="Course", to_field="id", on_delete=models.CASCADE, related_name='course_score',
                             db_column='c_id', help_text="学生编号")
    score = models.PositiveIntegerField("成绩",null=False,default=0,help_text="成绩")
    class Meta:
        db_table = "score"

#教师表
class Teacher(models.Model):
    t_name = models.CharField("老师姓名", max_length=64,null=False,help_text="老师姓名")

    class Meta:
        db_table="teacher"