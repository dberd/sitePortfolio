from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('portfolio/profile/', views.profile_view, name='profile'),
    path('portfolio/<str:username>/<int:portfolio_id>/', views.portfolio_detail_view, name='portfolio_detail'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
