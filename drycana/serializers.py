from rest_framework import serializers
from .models import MyModel, AffiliateApp, LocationType, Tag, Spot, SpotImage, SpotAffiliate

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

class SpotAffiliateSerializer(serializers.ModelSerializer):
    affiliate_app = AffiliateAppSerializer()

    class Meta:
        model = SpotAffiliate
        fields = ['affiliate_app', 'url']

class SpotSerializer(serializers.ModelSerializer):
    affiliate_apps = SpotAffiliateSerializer(source='spotaffiliate_set', many=True)
    main_image = serializers.SerializerMethodField()  # Add this line


    class Meta:
        model = Spot
        fields = '__all__'

    def create(self, validated_data):
        affiliate_apps_data = validated_data.pop('spotaffiliate_set')
        spot = Spot.objects.create(**validated_data)
        for affiliate_app_data in affiliate_apps_data:
            SpotAffiliate.objects.create(spot=spot, **affiliate_app_data)
        return spot

    def update(self, instance, validated_data):
        affiliate_apps_data = validated_data.pop('spotaffiliate_set')
        instance = super().update(instance, validated_data)

        # Handle the affiliate apps
        instance.spotaffiliate_set.all().delete()  # Remove existing relationships
        for affiliate_app_data in affiliate_apps_data:
            SpotAffiliate.objects.create(spot=instance, **affiliate_app_data)
        return instance
    
    def get_main_image(self, obj):
        main_image = obj.additional_images.filter(is_main_image=True).first()
        if main_image:
            return main_image.image.url
        return None

class SpotImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotImage
        fields = '__all__'
