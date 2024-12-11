from django.urls import path

from . import views

urlpatterns = [
    path('', views.logInView, name='logIn'),
    path('signUp/', views.signUpView, name='signUp'),
    path('forgotPassword/', views.forgotPasswordView, name='forgotPassword'),
    ]