from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ['username', 'title', 'gender', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Password and Confirm Password do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user
