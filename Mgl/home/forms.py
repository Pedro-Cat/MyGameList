from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    review = forms.CharField(
        required=False,
        label='',
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': "Write your review here!",
                'name': 'text',
                'maxLength': '1000',
                'rows': '5',
                'cols': '50',
                'required': 'True',
            }                         
            )
    )
    class Meta:
        model = Review
        fields = ('review', 'score')
