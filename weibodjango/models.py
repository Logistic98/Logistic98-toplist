from django.db import models

# Create your models here.

class Headline(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()

    # 按照发布时间进行排序（降序）
    class Meta:
        ordering = ['-publishTime']
