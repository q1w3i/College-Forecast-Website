from django.db import models
import hashlib

class User(models.Model):
    id = models.CharField(max_length=11,primary_key=True,verbose_name='id,唯一标识')
    username=models.CharField(max_length=11,verbose_name='用户名,登陆用')
    password = models.CharField(max_length=11,verbose_name='密码')
    email = models.CharField(max_length=255,verbose_name='邮箱')
    targetCollege = models.CharField(max_length=255, verbose_name='目标院校',blank=True)
    targetScore = models.IntegerField(verbose_name='理想成绩',blank=True)
    currentScore = models.IntegerField(verbose_name='当前成绩',blank=True)
    historyScore = models.IntegerField(verbose_name='历史成绩',blank=True)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        md5 = hashlib.md5()
        md5.update(self.password.encode())
        self.password = md5.hexdigest()
        super(User, self).save(*args, **kwargs)

class UpdateUser(models.Model):
    id = models.CharField(max_length=11,primary_key=True,verbose_name='id,唯一标识')
    username=models.CharField(max_length=11,verbose_name='用户名,登陆用')
    password = models.CharField(max_length=11,verbose_name='密码')
    email = models.CharField(max_length=255,verbose_name='邮箱')
    targetCollege = models.CharField(max_length=255, verbose_name='目标院校',blank=True)
    targetScore = models.IntegerField(verbose_name='理想成绩',blank=True)
    currentScore = models.IntegerField(verbose_name='当前成绩',blank=True)
    historyScore = models.IntegerField(verbose_name='历史成绩',blank=True)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.id
