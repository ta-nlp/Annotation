from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('annotate/', views.annotate, name='annoatate'),
    path('annotatefile/', views.annotateusingupload, name='annoatate'),
    path('help/', views.help, name='help'),
]