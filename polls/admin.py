# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['ques_text']}),
        ('Date information', {'fields': ['ques_date'], 
                              'classes': ['collapse']}),
    ]
    inlines= [ChoiceInline]
    list_display= ('ques_text','ques_date')

admin.site.register(Question,QuestionAdmin)
