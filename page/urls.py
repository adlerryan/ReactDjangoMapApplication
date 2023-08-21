from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'mymodel', views.MyModelViewSet)
router.register(r'affiliateapp', views.AffiliateAppViewSet)
router.register(r'locationtype', views.LocationTypeViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'spot', views.SpotViewSet)
router.register(r'spotimage', views.SpotImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
