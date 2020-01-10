from django import forms
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    author = forms.CharField(max_length=100, label='Author')
    content = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }),label='Content')
    email= forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = [
            'content',
            'author',
            'email'
        ]
