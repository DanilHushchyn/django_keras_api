from django.urls import path
from . import views


app_name = 'keras_model'
urlpatterns = [
    path('', views.index, name='index'),
    path('image/', views.predict_Image, name='image'),
]