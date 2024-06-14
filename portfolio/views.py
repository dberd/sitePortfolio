from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('portfolio')
    else:
        form = PortfolioForm()
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio/portfolio.html', {'form': form, 'portfolios': portfolios})

@login_required
def portfolio_detail_view(request, username, portfolio_id):
    user = get_object_or_404(User, username=username)
    portfolio = get_object_or_404(Portfolio, user=user, id=portfolio_id)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio})
