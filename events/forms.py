from django import forms
from .models import Testimony

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Rename form field IDs to match your HTML exactly
        self.fields['full_name'].widget.attrs.update({
            'id': 'name', 'placeholder': 'Full name', 'class': 'form-control', 'required': True
        })
        self.fields['email'].widget.attrs.update({
            'id': 'email', 'placeholder': 'Email address', 'class': 'form-control', 'required': True
        })
        self.fields['message'].widget.attrs.update({
            'id': 'message', 'placeholder': 'Leave a comment here', 'class': 'form-control', 'required': True, 'style': 'height: 160px'
        })
