# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import loader
from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_ques = Question.objects.order_by('-ques_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {"latest_ques":latest_ques,}
    return HttpResponse(template.render(context,request))

def details(request, question_id):
    try:
        ques = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    return render(request, 'polls/details.html',{"ques":ques,})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)