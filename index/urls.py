from django.urls import path
from .views import SearchView,  IndexView, ManagerView, FrontEndFacebook, RatingFormView, ConstructionView, SoftDevFacebook, DataScienceFacebook, FrontEndFacebookStudent, DataScienceFacebookStudent, SoftDevFacebookStudent, SoftDevASICSStudent

app_name = 'index'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('manager/', ManagerView.as_view(), name='manager'),
    path('manager/front-end-facebook/', FrontEndFacebook.as_view(), name='front-end-facebook-m'),
    path('manager/soft-dev-facebook/', SoftDevFacebook.as_view(), name='soft-dev-facebook-m'),
    path('manager/data-scientist-facebook/', DataScienceFacebook.as_view(), name='data-scientist-facebook-m'),
    path('search/front-end-facebook/', FrontEndFacebookStudent.as_view(), name='front-end-facebook-s'),
    path('search/soft-dev-facebook/', SoftDevFacebookStudent.as_view(), name='soft-dev-facebook-s'),
    path('search/data-scientist-facebook/', DataScienceFacebookStudent.as_view(), name='data-scientist-facebook-s'),
    path('search/soft-eng-ASICS/', SoftDevASICSStudent.as_view(), name='soft-eng-ASICS-s'),
    path('ratingform/', RatingFormView.as_view(), name='ratingform'),
    path('construction/', ConstructionView.as_view(), name='construction'),
]
