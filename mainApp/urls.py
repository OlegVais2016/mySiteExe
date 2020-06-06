
from django.urls import include, path
from . import views

urlpatterns = [

    path('mainApp/', views.index, name='index'),

]