from django.urls import path
from . import views
urlpatterns = [
    path('', views.fileupload, name='fileupload'),
    path('post/', views.postupload, name='postupload'),
]