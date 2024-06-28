from django import forms
from .models import UserModel
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel


        fields = ['name', 'age', 'email', 'gender', 'governorate', 'cs_field', 'experience_levels', 'twitter_link',
                  'github_link', 'buddy_age', 'buddy_gender', 'buddy_governorate']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-field'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-field'}),
            'age': forms.Select(attrs={'class': 'form-field'}),
            'gender': forms.Select(attrs={'class': 'form-field'}),
            'governorate': forms.Select(attrs={'class': 'form-field'}),
            'cs_field': forms.Select(attrs={'class': 'form-field'}),
            'experience_levels': forms.Select(attrs={'class': 'form-field'}),
            'twitter_link': forms.TextInput(attrs={'placeholder': 'Twitter link', 'class': 'form-field'}),
            'github_link': forms.TextInput(attrs={'placeholder': 'Github link', 'class': 'form-field'}),
            'buddy_age': forms.Select(attrs={'class': 'form-field'}),
            'buddy_gender': forms.Select(attrs={'class': 'form-field'}),
            'buddy_governorate': forms.Select(attrs={'class': 'form-field'}),
        }

