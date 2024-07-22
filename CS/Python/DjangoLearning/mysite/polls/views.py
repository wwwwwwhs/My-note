'''
Author: 崩布猪
Date: 2024-04-27 09:21:22
LastEditors: 崩布猪
LastEditTime: 2024-04-27 09:46:51
FilePath: \mysite\polls\views.py
Description:  this is a view function

'''
from django.shortcuts import HttpResponse
from .models import Question
from django.template import loader
# Create your views here.

def index(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "Latest_question_list": lastest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(requset, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(requset, question_id):
    return HttpResponse("You're voting on question %s." % question_id)