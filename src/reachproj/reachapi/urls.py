from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^ridepostings/create/$',
        views.RidePostingCreateAPIView.as_view()),
    url(r'^ridepostings/(?P<pk>[0-9]+)/$',
        views.RidePostingRUDAPIView.as_view()),
    url(r'^ridepostings/(?P<pk>[0-9]+)/accept/$',
        views.RidePostingAcceptView.as_view()),
    url(r'^ridepostings/(?P<pk>[0-9]+)/offer/$',
        views.RidePostingOfferView.as_view()),
    url(r'^ridepostings/$',
        views.RidePostingListView.as_view()),
    url(r'^riderequests/create/$',
        views.RideRequestCreateAPIView.as_view()),
    url(r'^riderequests/(?P<pk>[0-9]+)/$',
        views.RideRequestRUDAPIView.as_view()),
    url(r'^riderequests/(?P<pk>[0-9]+)/accept/$',
        views.RideRequestAcceptView.as_view()),
    url(r'^riderequests/(?P<pk>[0-9]+)/offer/$',
        views.RideRequestOfferView.as_view()),
    url(r'^riderequests/$',
        views.RideRequestListView.as_view()),
    url(r'^places/create/$',
        views.PlaceCreateView.as_view()),
])
