from django.urls import path
from .views import SearchView,  IndexView, ManagerView, PositionView, RatingFormView

app_name = 'index'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('manager/', ManagerView.as_view(), name='manager'),
    path('front-end-facebook/', PositionView.as_view(), name='front-end-facebook'),
    path('ratingform/', RatingFormView.as_view(), name='ratingform'),
]
