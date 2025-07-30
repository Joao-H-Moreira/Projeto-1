from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    return HttpResponse("<h1> Bem-vindo à pàgina de Receitas!</h1> ")