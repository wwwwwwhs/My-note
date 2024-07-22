'''
Author: 崩布猪
Date: 2024-04-27 09:21:22
LastEditors: 崩布猪
LastEditTime: 2024-04-27 11:52:31
FilePath: \mysite\polls\models.py
Description: 

'''
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    '''问题模型 包含问题描述 和 发布时间'''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    '''选项模型 包含选项描述 和 当前投票数'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text