from django.urls import path
from . import views
from .views import display,ProfileView,Data
from django.conf import settings
from django.conf.urls.static import static

app_name = 'caretaker'

urlpatterns = [
    
    path('display', views.display, name='display'),
    path('', views.index , name="index"),
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    path('forms/',Data.as_view(),name="Data")
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


