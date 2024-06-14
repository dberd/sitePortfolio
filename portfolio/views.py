from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, PortfolioForm
from .models import Portfolio

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portfolio')
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль')
    else:
        form = LoginForm()

    return render(request, 'portfolio/login.html', {'form': form})

def index(request):
    return render(request, 'portfolio/index.html')

@login_required
def portfolio_view(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio/portfolio.html', {'form': form})
