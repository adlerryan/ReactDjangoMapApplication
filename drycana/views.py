from rest_framework import viewsets
from .models import MyModel, AffiliateApp, LocationType, Tag, Spot, SpotImage
from .serializers import MyModelSerializer, AffiliateAppSerializer, LocationTypeSerializer, TagSerializer, SpotSerializer, SpotImageSerializer
from django.views.generic import TemplateView


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class AffiliateAppViewSet(viewsets.ModelViewSet):
    queryset = AffiliateApp.objects.all()
    serializer_class = AffiliateAppSerializer

class LocationTypeViewSet(viewsets.ModelViewSet):
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

class SpotImageViewSet(viewsets.ModelViewSet):
    queryset = SpotImage.objects.all()
    serializer_class = SpotImageSerializer


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'