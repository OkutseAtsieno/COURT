from django import forms
from django.contrib.auth.models import User
from .models import Profile, Advocate

# Define the role choices for the dropdown
ROLE_CHOICES = [
    ('advocate', 'Advocate'),
    ('user', 'User'),
    ('clerk', 'Clerk'),
]

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    # ChoiceField to allow users to select between Advocate, User, and Client
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select)

    class Meta:
        model = Profile
        fields = ['role']

class AdvocateForm(forms.ModelForm):
    class Meta:
        model = Advocate
        fields = [
            'bar_number',
            'specialty',
            'years_of_experience',
            'phone_number',
            'email',
            'address',
            'firm',
            'license_issued_date',
            'is_active'
        ]
