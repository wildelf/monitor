from django.db import models

# Create your models here.

class Host(models.Model):
    machine_id = models.CharField(max_length=50, verbose_name="机器编号", unique=True)

    def __str__(self):
        return self.machine_id


class ProcessData(models.Model):
    date = models.DateTimeField(auto_now_add=True,verbose_name='日期')
    name = models.CharField(max_length=50,verbose_name='进程名')
    percent = models.FloatField(max_length='50',verbose_name='百分比')
    host = models.ForeignKey('Host',on_delete=models.CASCADE)
    def __str__(self):
        return self.name