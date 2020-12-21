from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        # Call save of the super of your own class,
        # which is UserCreationForm.save() which calls user.set_password()
        user = super(UserCreateForm, self).save(commit=False)

        # Add the things your super doesn't do for you
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
