from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章列表"

    def __str__(self):
        return self.title
