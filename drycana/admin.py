from django.contrib import admin
from .models import Spot, AffiliateApp, LocationType, Tag, SpotImage, SpotAffiliate

class SpotImageInline(admin.TabularInline):
    model = SpotImage

class SpotAffiliateInline(admin.TabularInline):
    model = SpotAffiliate
    extra = 1

@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude', 'website')
    search_fields = ('name', 'address')
    inlines = [SpotImageInline, SpotAffiliateInline]

admin.site.register(AffiliateApp)
admin.site.register(LocationType)
admin.site.register(Tag)
