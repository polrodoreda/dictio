from django.urls import path

from core.views import HomeView, DictionariesView, DictionaryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dictionaries/', DictionariesView.as_view(), name='dictionaries'),
    path('dictionaries/<int:pk>/', DictionaryView.as_view(), name='dictionary')
]
