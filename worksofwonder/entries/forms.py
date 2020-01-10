from django import forms
from django.contrib.auth.models import User


class ArticleForm(forms.Form):
    author = forms.CharField(max_length=100, label='author')
    content = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))
    email= forms.EmailField()

    class Meta:
        model = User
        fields = [
            'author',
            'content',
            'email'
        ]
