"""
URL configuration for drycana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from . import views
# from page import views


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     # path('', views.index),
#     path('page/', include('page.urls')),
#     path('api/spots/', views.get_spot_details, name='spot_details'),
#     path('api/page/spots/', views.get_spot_details, name='get_all_spots'),
#     path('admin/page/spot/', views.get_spot_details, name='admin_spot_details'),
#     path('api/affiliate_apps/', views.get_all_affiliate_apps, name='get_all_affiliate_apps'),
#     path('api/location_types/', views.get_all_location_types, name='get_all_location_types'),
#     path('api/tags/', views.get_all_tags, name='get_all_tags'),
# ]

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib import admin
from django.urls import path, include
from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'mymodel', views.MyModelViewSet)
router.register(r'affiliateapp', views.AffiliateAppViewSet)
router.register(r'locationtype', views.LocationTypeViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'spot', views.SpotViewSet)
router.register(r'spotimage', views.SpotImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)