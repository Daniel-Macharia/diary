from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('addMemory/', views.addMemoryView, name='addMemory'),
    path('review/', views.reviewMemoryView, name='review')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)