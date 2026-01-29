from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def MainFunc(request):
    #return HttpResponse('Главная функция главной страницы главного блока')
    return render(request, 'main.html')

def RegFunc(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Сохраняем пользователя
            user = form.save()
            
            # Автоматически логиним пользователя
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Перенаправляем на главную страницу после успешной регистрации
                return redirect('main')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})