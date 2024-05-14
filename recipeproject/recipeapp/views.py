from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def index(request):
    return HttpResponse('Рецепты')

class Index(TemplateView):
    template_name = 'recipeapp/base.html'


