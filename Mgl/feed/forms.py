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
                'placeholder': "what's up!?",
                'name': 'text',
                'maxLength': '320',
                'rows': '2',
                'cols': '10',
                'required': 'True',
            }                         
            )
        )

    archive = forms.FileField(
        required=False,
        label='',
        widget=forms.widgets.ClearableFileInput(
            attrs={
                'class': 'btn btn-outline-primary dropdown-toggle',
            }
        )
        )

    class Meta:
        model = Post
        #fields = ('body', 'archive')
        exclude = ('user', 'likes', 'post_father', 'edited', 'deleted', 'filed',)
