from django import forms

class ArticleForm(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    content = forms.Textarea()
