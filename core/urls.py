from django.urls import path

from core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dictionaries/', views.DictionariesView.as_view(), name='dictionaries'),
    path('dictionaries/<int:pk>/', views.DictionaryView.as_view(), name='dictionary'),
    path('word/add/', views.add_word, name='add_word')
]
