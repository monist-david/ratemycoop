from django.urls import path
from .views import SearchView

app_name = 'index'
urlpatterns = [
    path('', SearchView.as_view(), name='index'),
]
