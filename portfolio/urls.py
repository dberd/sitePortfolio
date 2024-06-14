from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
