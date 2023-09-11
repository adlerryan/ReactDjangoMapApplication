from django.contrib import admin
from django import forms
from django.forms.widgets import Select
from django.db import connections
from .models import Spot, AffiliateApp, LocationType, Tag, SpotImage, SpotAffiliate, MenuItem, CodeInterpreter

# Custom Time Widget
HOUR_CHOICES = [(str(i), str(i)) for i in range(1, 13)]
AM_PM_CHOICES = [('AM', 'AM'), ('PM', 'PM')]

class SimpleTimeWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            Select(attrs=attrs, choices=HOUR_CHOICES),
            Select(attrs=attrs, choices=AM_PM_CHOICES)
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.strftime('%I'), value.strftime('%p')]
        return [None, None]

# SpotAdminForm with custom fields
class SpotAdminForm(forms.ModelForm):
    monday_open_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    monday_open_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)
    monday_close_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    monday_close_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)

    tuesday_open_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    tuesday_open_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)
    tuesday_close_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    tuesday_close_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)

    wednesday_open_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    wednesday_open_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)
    wednesday_close_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    wednesday_close_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)

    thursday_open_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    thursday_open_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)
    thursday_close_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    thursday_close_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)

    friday_open_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    friday_open_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)
    friday_close_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    friday_close_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)

    saturday_open_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    saturday_open_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)
    saturday_close_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    saturday_close_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)

    sunday_open_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    sunday_open_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)
    sunday_close_hour = forms.ChoiceField(choices=HOUR_CHOICES)
    sunday_close_ampm = forms.ChoiceField(choices=AM_PM_CHOICES)

    class Meta:
        model = Spot
        fields = '__all__'

# Admin classes and inlines
class SpotImageInline(admin.TabularInline):
    model = SpotImage

class SpotAffiliateInline(admin.TabularInline):
    model = SpotAffiliate
    extra = 1

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    form = SpotAdminForm  # Use the custom form
    list_display = (
        'name', 'address', 'latitude', 'longitude', 'website'
    )
    search_fields = ('name', 'address')
    inlines = [SpotImageInline, SpotAffiliateInline, MenuItemInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'address', 'latitude', 'longitude', 'website')
        }),
        ('Hours', {
            'fields': (
                ('monday_open_hour', 'monday_open_ampm', 'monday_close_hour', 'monday_close_ampm'),
                ('tuesday_open_hour', 'tuesday_open_ampm', 'tuesday_close_hour', 'tuesday_close_ampm'),
                ('wednesday_open_hour', 'wednesday_open_ampm', 'wednesday_close_hour', 'wednesday_close_ampm'),
                ('thursday_open_hour', 'thursday_open_ampm', 'thursday_close_hour', 'thursday_close_ampm'),
                ('friday_open_hour', 'friday_open_ampm', 'friday_close_hour', 'friday_close_ampm'),
                ('saturday_open_hour', 'saturday_open_ampm', 'saturday_close_hour', 'saturday_close_ampm'),
                ('sunday_open_hour', 'sunday_open_ampm', 'sunday_close_hour', 'sunday_close_ampm'),
            ),
        }),
    )

def get_table_choices():
    # Get the default database connection
    connection = connections['default']
    # Use introspection to get a list of all table names
    tables = connection.introspection.table_names()
    # Convert the list of table names into the format needed for form choices
    return [(table, table) for table in tables]

class CodeInterpreterForm(forms.ModelForm):
    table = forms.ChoiceField(choices=get_table_choices())

    class Meta:
        model = CodeInterpreter
        fields = ['language', 'table', 'code']

@admin.register(CodeInterpreter)
class CodeInterpreterAdmin(admin.ModelAdmin):
    form = CodeInterpreterForm
    list_display = ['language', 'table', 'code', 'result']

    
admin.site.register(AffiliateApp)
admin.site.register(LocationType)
admin.site.register(Tag)





# from django import forms
# from django.contrib import admin
# from django.contrib.admin.widgets import AdminTimeWidget
# from .models import Spot, AffiliateApp, LocationType, Tag, SpotImage, SpotAffiliate, MenuItem

# # Create a custom form for the Spot model
# class SpotAdminForm(forms.ModelForm):
#     monday_open = forms.TimeField(widget=AdminTimeWidget())
#     monday_close = forms.TimeField(widget=AdminTimeWidget())
#     tuesday_open = forms.TimeField(widget=AdminTimeWidget())
#     tuesday_close = forms.TimeField(widget=AdminTimeWidget())
#     wednesday_open = forms.TimeField(widget=AdminTimeWidget())
#     wednesday_close = forms.TimeField(widget=AdminTimeWidget())
#     thursday_open = forms.TimeField(widget=AdminTimeWidget())
#     thursday_close = forms.TimeField(widget=AdminTimeWidget())
#     friday_open = forms.TimeField(widget=AdminTimeWidget())
#     friday_close = forms.TimeField(widget=AdminTimeWidget())
#     saturday_open = forms.TimeField(widget=AdminTimeWidget())
#     saturday_close = forms.TimeField(widget=AdminTimeWidget())
#     sunday_open = forms.TimeField(widget=AdminTimeWidget())
#     sunday_close = forms.TimeField(widget=AdminTimeWidget())

#     class Meta:
#         model = Spot
#         fields = '__all__'


# class SpotImageInline(admin.TabularInline):
#     model = SpotImage

# class SpotAffiliateInline(admin.TabularInline):
#     model = SpotAffiliate
#     extra = 1

# @admin.register(Spot)
# class SpotAdmin(admin.ModelAdmin):
#     form = SpotAdminForm  # Use the custom form
#     list_display = (
#         'name', 'address', 'latitude', 'longitude', 'website'
#     )
#     search_fields = ('name', 'address')
#     inlines = [SpotImageInline, SpotAffiliateInline]
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'address', 'latitude', 'longitude', 'website')
#         }),
#         ('Hours', {
#             'fields': (
#                 ('monday_open', 'monday_close'),
#                 ('tuesday_open', 'tuesday_close'),
#                 ('wednesday_open', 'wednesday_close'),
#                 ('thursday_open', 'thursday_close'),
#                 ('friday_open', 'friday_close'),
#                 ('saturday_open', 'saturday_close'),
#                 ('sunday_open', 'sunday_close')
#             ),
#         }),
#     )

# admin.site.register(AffiliateApp)
# admin.site.register(LocationType)
# admin.site.register(Tag)
# admin.site.register(MenuItem)
