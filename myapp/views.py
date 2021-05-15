from django.shortcuts import render,HttpResponse
from myapp import models
from django.http import JsonResponse
from django.db import transaction
from bs4 import BeautifulSoup


# Create your views here.


def index(request):
	article_list = models.Article.objects.filter(title__icontains="教程",classify="基础知识")
	article_web_intro = models.Article.objects.filter(title__icontains="教程",classify="相关知识")
	return render(request, "index.html", {"article_list": article_list,"article_web_intro":article_web_intro})


def article_detail(request, programming_tools, english_title):
	# print(programming_tools)
	# print(english_title)
	
	article_list = models.Article.objects.filter(programming_tools=programming_tools,classify="基础知识").all()
	article_list_related = models.Article.objects.filter(programming_tools=programming_tools, classify="相关知识").all()
	article_cont = models.Article.objects.filter(english_title=english_title).values("content")
	article_content = article_cont[0]["content"]
	article_tit = models.Article.objects.filter(english_title=english_title).values("title")
	article_title = article_tit[0]["title"]
	article_id_qs = models.Article.objects.filter(english_title=english_title).values("nid")
	article_id = article_id_qs[0]["nid"]
	
	comment_list = models.Comment.objects.filter(article_id=article_id)

	return render(request, 'articledetail.html',
	              {
		              "article_list": article_list,
		              "article_content": article_content,
		              "article_title": article_title,
		              "article_id":article_id,
		              "comment_list":comment_list,
		              "article_list_related":article_list_related
		              
	              }
	              )


def comment(request):
	article_id = request.POST.get("article_id")
	content = request.POST.get("content")
	username = request.POST.get("username")
	
	soup = BeautifulSoup(content,"html.parser")
	for tag in soup.find_all():
		if tag.name == "script":
			tag.decompose()

	with transaction.atomic():
		comment_obj = models.Comment.objects.create(article_id=article_id, content=str(soup), username=username)
	
	response = {}
	response["create_time"] = comment_obj.create_time.strftime("%Y-%m-%d %X")
	response["username"] = username
	response["content"] = content
	
	return JsonResponse(response)

