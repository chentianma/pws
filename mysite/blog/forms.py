from django import forms
from .models import Article
from django.contrib.auth.models import User


class postForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'description', 'text', 'category', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', }))
        # description = forms.Textarea()
        # text = forms.Textarea()
        # category = forms.Select()
        # tags = forms.SelectMultiple()


# class NewUserForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         widgets = {
#             'username': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Username', }),
#             'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', })
#         }