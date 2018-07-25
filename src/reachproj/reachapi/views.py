from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import PlaceSerializer, ProfileSerializer, RidePostingSerializer, RideRequestSerializer, RidePostingAcceptSerializer

from .models import RidePosting, RideRequest, Profile
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

# Create your views here.
class PlaceCreateView(CreateAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)#This will need to be changed to implement social auth
    permission_classes = (AllowAny,)
    serializer_class = PlaceSerializer

#User does not need to be signed in (authenticated) to access this view
class RidePostingListView(ListAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)#This will need to be changed to implement social auth
    permission_classes = (AllowAny,)
    serializer_class = RidePostingSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `price` query parameter in the URL.
        """
        queryset = RidePosting.objects.all()
        desired_price = self.request.query_params.get('price', None)
        desired_seats = self.request.query_params.get('seats', None)
        if desired_price is not None:
            queryset = queryset.filter(price__lte= desired_price)
        if desired_seats is not None:
            queryset = queryset.filter(seats_left__gte=desired_seats)

        return queryset

#User needs to be signed in (authenticated) to use this create view
class RidePostingCreateAPIView(CreateAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RidePostingSerializer

#User must be owner to perform PUT or DELETE requests
class RidePostingRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = RidePostingSerializer

class RidePostingAcceptView(RetrieveUpdateAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RidePostingAcceptSerializer

class RideRequestListView(ListAPIView):
    queryset = RideRequest.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    serializer_class = RideRequestSerializer

class RideRequestCreateAPIView(CreateAPIView):
    queryset = RideRequest.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RideRequestSerializer

class RideRequestRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = RideRequest.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = RideRequestSerializer

class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    serializer_class = RideRequestSerializer

class ProfileCreateAPIView(CreateAPIView):
    queryset = Profile.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RideRequestSerializer

class ProfileRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = RideRequestSerializer
