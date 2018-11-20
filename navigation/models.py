from django.db import models


# Create your models here.
class Navi(models.Model):
    name = models.CharField("名称", max_length=20)
    url = models.URLField("网址")
    description = models.CharField("描述", max_length=50)

    def __str__(self):
        return self.name
