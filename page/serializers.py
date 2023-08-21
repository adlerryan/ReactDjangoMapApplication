from rest_framework import serializers
from .models import MyModel, AffiliateApp, LocationType, Tag, Spot, SpotImage

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

class AffiliateAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateApp
        fields = '__all__'

class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'

class SpotImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotImage
        fields = '__all__'
