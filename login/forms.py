#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
#registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from django.shortcuts import render,get_object_or_404,redirect
from django.core.exceptions import ValidationError

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
							   
class SignUpForm(UserCreationForm):

    def no_future(value):
        today = datetime.date.today()
        if value > today:
            raise ValidationError('date of birth cannot be in the future.')
    
    first_name=forms.CharField(widget=forms.TextInput)
    last_name=forms.CharField(widget=forms.TextInput)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD',validators=[no_future])
    
    
    FAVORITE_ARTICLE_CHOICES = [('1', 'POLITICS'), ('2', 'SPORTS'),('3', 'TECHNOLOGY'), ('2', 'HEALTH')]
    Artcle_preference= forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_ARTICLE_CHOICES,)
	
class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2','first_name','last_name', )
