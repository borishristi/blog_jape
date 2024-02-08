from django.urls import path

from articles import views

urlpatterns = [
    path('', views.articles_view, name='articles_view'),
]
