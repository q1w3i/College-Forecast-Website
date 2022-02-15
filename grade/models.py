from django.db import models

class Grade(models.Model):
    year = models.IntegerField(primary_key=True,verbose_name='年份')
    bk1 = models.FloatField(verbose_name='一本线')
    bk2 = models.FloatField(verbose_name='二本线')
    bk3 = models.FloatField(verbose_name='三本线')
    isAnalysis = models.BooleanField(verbose_name='是否预测值',default=False, blank=True)

    class Meta:
        db_table = 'zhejiang'

    def __str__(self):
        return self.year