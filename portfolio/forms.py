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
        fields = ['bio', 'academic_achievements', 'projects', 'work_experience', 'documents']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'academic_achievements': forms.Textarea(attrs={'class': 'form-control'}),
            'projects': forms.Textarea(attrs={'class': 'form-control'}),
            'work_experience': forms.Textarea(attrs={'class': 'form-control'}),
        }
