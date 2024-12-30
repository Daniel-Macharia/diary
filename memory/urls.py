from django.urls import path
from . import views

urlpatterns = [
    path('addMemory/', views.addMemoryView, name='addMemory'),
    path('review/', views.reviewMemoryView, name='review')
]