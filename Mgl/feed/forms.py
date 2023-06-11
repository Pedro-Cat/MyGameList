from django.forms import ModelForm
from django import forms

from .models import Post

# Create PostForms
class PostForms(ModelForm):
    body = forms.CharField(
        required=False,
        label='',
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': 'What are you thinking?',
                'class': 'form-control',
                'required': 'True',
            }                         
            )
        )

    archive = forms.FileField(required=False, label='')

    class Meta:
        model = Post
        #fields = ('body', 'archive')
        exclude = ('user', 'likes', 'post_father', 'edited', 'deleted', 'filed',)
