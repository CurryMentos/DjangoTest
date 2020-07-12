from django.db import models


# Create your models here.

class Student(models.Model):
    s_name = models.CharField(max_length=64, help_text="学生姓名")
    s_sex = models.IntegerField(choices=((0, '男'), (1, '女')), help_text="性别")
    s_phone = models.CharField(max_length=11, help_text="手机号")
    # auto_now_add=True 在每一次数据被添加进去的时候，记录当前时间
    create_time = models.DateTimeField(auto_now_add=True)
    # auto_now=True 在每一次数据被保存的时候，记录当前时间
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student'  # 指定表名

