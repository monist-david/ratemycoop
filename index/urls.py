from django.urls import path
from .views import SearchView,  IndexView, ManagerView, FrontEndFacebook, RatingFormView, ConstructionView, SoftDevFacebook, DataScienceFacebook

app_name = 'index'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('manager/', ManagerView.as_view(), name='manager'),
    path('front-end-facebook/', FrontEndFacebook.as_view(), name='front-end-facebook'),
    path('soft-dev-facebook/', SoftDevFacebook.as_view(), name='soft-dev-facebook'),
    path('data-scientist-facebook/', DataScienceFacebook.as_view(), name='data-scientist-facebook'),
    path('ratingform/', RatingFormView.as_view(), name='ratingform'),
    path('construction/', ConstructionView.as_view(), name='construction'),
]
