from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Article(models.Model):
	nid = models.AutoField(primary_key=True)
	programming_tools = models.CharField(verbose_name='编程工具', max_length=50)
	title = models.CharField(verbose_name='文章标题', max_length=50)
	english_title = models.CharField(verbose_name='英文标题', max_length=50)
	classify = models.CharField(verbose_name='内容分类', max_length=50)
	create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
	content = RichTextUploadingField(verbose_name='正文')

	def __str__(self):
		return self.title


class Comment(models.Model):

	nid = models.AutoField(primary_key=True)
	username = models.CharField(verbose_name='评论昵称', max_length=50)
	article = models.ForeignKey(verbose_name='评论文章', to='Article', to_field='nid',on_delete=models.CASCADE)
	content = models.TextField(verbose_name='评论内容')
	create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
	
	def __str__(self):
		return self.content

