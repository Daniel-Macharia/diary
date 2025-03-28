from django.shortcuts import render
from django.http import HttpResponse

from django.db import connection

from . import forms
from . import models

# Create your views here.
def logInView(request):
    if request.method == 'POST':
        name = request.POST.get('userName')
        password = request.POST.get('userPassword')

        cursor = connection.cursor()

        q_set = cursor.execute("SELECT userID, userName FROM userAuth_User WHERE userName LIKE %s AND userPassword LIKE %s", [f"{name}", f"{password}"])#.filter(userName=name)

        user = q_set.fetchone()
        print(user)
        if user:
            return render(request, 'memory/home.html')
        else:
            return HttpResponse("No user with the entered name exists!\nPlease sign up.")
        
        """userListIsEmpty = True
        for user in users:
            userListIsEmpty = False
            if user.userName == name:
                if user.userPassword == password:
                    #allow log in
                    return render(request, 'memory/home.html')
        
        if userListIsEmpty:
            return HttpResponse("No user with the entered name exists!\nPlease sign up.")
        else:
            return HttpResponse("Wrong password!\nPlease confirm and re-try")
    """
    else:
        logInForm = forms.UserLogInForm()
        return render(request, 'userAuth/logIn.html', {'form' : logInForm})
    


def signUpView(request):
    if request.method == 'POST':
        userData = forms.UserSignUpForm(request.POST)
        if not userData.is_valid():
            profilePicture = request.FILES.get('userProfilePicture')
            name = request.POST.get('userName')
            email = request.POST.get('userEmail')
            password = request.POST.get('userPassword')
            confirmPassword = request.POST.get('confirmPassword')

            if password == confirmPassword:
                user = models.User(userProfilePicture=Null, userName=name, userEmail=email, userPassword=password)
                user.save()
                return render( request, "memory/home.html")
            else:
                return HttpResponse(f"Password({password}) and confirm password({confirmPassword}) do not match")
        else:
            return HttpResponse(f"Invalid details!\n\nForm: {userData}")
        
    else:
        signUpForm = forms.UserSignUpForm()
        return render(request, "userAuth/signUp.html", {'form' : signUpForm})


def forgotPasswordView(request):
    return HttpResponse("Forgot password page...")
        
