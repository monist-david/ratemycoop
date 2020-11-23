from django.urls import path
from .views import SearchView,  IndexView, RatingFormView

app_name = 'index'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('ratingform/', RatingFormView.as_view(), name='ratingform'),
]
