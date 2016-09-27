from django import forms
from .models import Article


class postForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'description', 'text', 'category', 'tags')