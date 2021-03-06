from rest_framework import serializers
from .models import Place, Profile, RideRequest, RidePosting

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('city',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email','name','user','age','rating','num_ratings','num_rides','friendlist','phone_num')

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ('__all__')
        
class RideRequestOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ('offered_drivers')
        
class RideRequestAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ('requested_drivers', 'request_completed')

class RidePostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RidePosting
        fields = ('__all__')
        #fields = ('dest','start','user','date','time_min','time_max','price','seats','seats_left','description','confirmed_riders','potential_riders','stops')

class RidePostingOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = RidePosting
        fields = ('offered_riders')
        
class RidePostingAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = RidePosting
        fields = ('seats','confirmed_riders')

#User serializer???
