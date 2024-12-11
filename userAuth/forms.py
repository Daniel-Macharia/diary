from django.forms import ModelForm
from . import models


class UserSignUpForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['userProfilePicture', 'userName', 'userEmail', 'userPassword']

    


class UserLogInForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['userName', 'userPassword']

    
