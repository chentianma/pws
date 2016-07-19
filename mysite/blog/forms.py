from django import forms
from .models import Article



class postForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'category', 'tags')
