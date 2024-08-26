from django.db import models

CHOICE = (('danger', 'high'), ('warning', 'normal'), ('info', 'low'))

# Create your models here.
class MemoModel(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField()
    priority = models.CharField(max_length=50 ,
                                choices = CHOICE)
    duedate = models.DateField()
    
    objects = models.Manager()
    
    # DBのデータを管理画面に表示させる
    def __str__(self):
        return self.title
 