from django.db import models

# Create your models here.

class Host(models.Model):
    machine_id = models.CharField(max_length=50, verbose_name=u"机器编号", unique=True)
    hostname = models.CharField(max_length=50, verbose_name=u"主机名", unique=True)


    def __unicode__(self):
        return self.hostname


