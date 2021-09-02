from django.db import models

# Create your models here.
class Article(models.Model):
  title=models.CharField('标题',max_length=70)  #创建字符类型
  content=models.TextField('内容',max_length=200,blank=True)  #创建文本类型   blank是否允许为空
  created_time=models.DateTimeField('发布时间')
  class Meta:
    verbose_name='文章'
    verbose_name_plural='文章'

  def __str__(self):
    return self.title

#所有的模型都必须要继承来自models.Model
class Category(models.Model):
  name=models.CharField('分类',max_length=100)

class Tags(models.Model):
  name=models.CharField('标签',max_length=100)


# class Article(models.Model):
#   ...
#   category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类',default='1')
#   tags=models.ManyToManyField(Tags,blank=True)

#   user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
#   created_time=models.DateTimeField('发布时间',auto_now_add=True)

  #模型创建好之后  其实就是相当于对应的表，将其迁移到数据库中。      python manage.py makemigrations

