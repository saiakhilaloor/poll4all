# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_ques = Question.objects.order_by('-ques_date')[:5]
    output = ','.join(q.ques_text for q in latest_ques)
    return HttpResponse(output)

def details(request, question_id):
    return HttpResponse("This is Question number : %s" %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)