from django.urls import path
from .views import UserAPIView, SpecificUserAPIView, MemoryAPIView, SpecificMemoryAPIView


urlpatterns = [
    path('user/<int:pk>/', SpecificUserAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    
    path('memory/<int:pk>/', SpecificMemoryAPIView.as_view()),
    path('memory/', MemoryAPIView.as_view()),
]