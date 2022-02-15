from django.db import models

class Seventeen(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='院校id')
    college = models.CharField(max_length=255,verbose_name='院校名字')
    grade = models.IntegerField(verbose_name='分数线')
    ranking = models.IntegerField(verbose_name='排位')

    class Meta:
        db_table = '2017'

    def __str__(self):
        return self.id

class Eighteen(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='院校id')
    college = models.CharField(max_length=255,verbose_name='院校名字')
    grade = models.IntegerField(verbose_name='分数线')
    ranking = models.IntegerField(verbose_name='排位')

    class Meta:
        db_table = '2018'

    def __str__(self):
        return self.id

class Nineteen(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='院校id')
    college = models.CharField(max_length=255,verbose_name='院校名字')
    grade = models.IntegerField(verbose_name='分数线')
    ranking = models.IntegerField(verbose_name='排位')

    class Meta:
        db_table = '2019'

    def __str__(self):
        return self.id

class Twenty(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='院校id')
    college = models.CharField(max_length=255,verbose_name='院校名字')
    grade = models.IntegerField(verbose_name='分数线')
    ranking = models.IntegerField(verbose_name='排位')

    class Meta:
        db_table = '2020'

    def __str__(self):
        return self.id