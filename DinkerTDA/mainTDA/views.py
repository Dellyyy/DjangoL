from django.shortcuts import render
from django.http import HttpResponse

def MainFunc(request):
    #return HttpResponse('Главная функция главной страницы главного блока')
    return render(request, 'main.html')
