from rest_framework import viewsets
from .models import MyModel, AffiliateApp, LocationType, Tag, Spot, SpotImage
from .serializers import MyModelSerializer, AffiliateAppSerializer, LocationTypeSerializer, TagSerializer, SpotSerializer, SpotImageSerializer
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db import connection


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

def execute_code(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        language = request.POST.get('language')
        table = request.POST.get('table')
        code = request.POST.get('code')

        if language == 'SQL':
            with connection.cursor() as cursor:
                cursor.execute(code)
                results = cursor.fetchall()
            return JsonResponse({'results': results})

        elif language == 'Python':
            # Caution: Executing arbitrary Python code can be dangerous.
            # Ensure you have proper safeguards in place.
            exec(code)
            # Handle the results as needed
            return JsonResponse({'results': 'Python code executed'})

    return JsonResponse({'error': 'Invalid request'}, status=400)