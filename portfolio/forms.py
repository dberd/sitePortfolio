from django import forms
from .models import Portfolio

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'title', 'full_name', 'about_me', 'course_work', 'conferences',
            'practices', 'skills', 'extracurricular_activities', 'documents', 'avatar'
        ]
        labels = {
            'title': 'Название портфолио',
            'full_name': 'ФИО',
            'about_me': 'О себе',
            'course_work': 'Выполнение курсовой и дипломной работ',
            'conferences': 'Участие в научно-практических студенческих конференциях',
            'practices': 'Опыт прохождения практик',
            'skills': 'Уровень профессиональных умений',
            'extracurricular_activities': 'Участие во внеучебной деятельности',
            'documents': 'Загрузить документы',
            'avatar': 'Аватар',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control'}),
            'course_work': forms.Textarea(attrs={'class': 'form-control'}),
            'conferences': forms.Textarea(attrs={'class': 'form-control'}),
            'practices': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control'}),
            'extracurricular_activities': forms.Textarea(attrs={'class': 'form-control'}),
            'documents': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
