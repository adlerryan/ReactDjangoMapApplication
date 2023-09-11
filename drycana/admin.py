
from django.contrib import admin, messages
from django import forms
from django.forms.widgets import Select
from django.db import connections, connection
from .models import Spot, AffiliateApp, LocationType, Tag, SpotImage, SpotAffiliate, MenuItem, CodeInterpreter
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

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
# ________________________ CODE INTERPRETER ___________________________
class CodeInterpreterAdmin(admin.ModelAdmin):
    form = CodeInterpreterForm
    list_display = ['language', 'table', 'code', 'result']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        # Execute the code when a new record is saved
        if obj.language == 'SQL':
            try:
                with connection.cursor() as cursor:
                    cursor.execute(obj.code)
                    column_headers = [col[0] for col in cursor.description]
                    results = cursor.fetchall()
                obj.result = str((column_headers, results))
                obj.save()
                messages.success(request, 'SQL code executed successfully.')
            except Exception as e:
                messages.error(request, f'Error executing SQL: {e}')
        
        elif obj.language == 'Python':
            # Caution: Executing arbitrary Python code can be dangerous.
            # Ensure you have proper safeguards in place.
            try:
                exec(obj.code)
                messages.success(request, 'Python code executed successfully.')
            except Exception as e:
                messages.error(request, f'Error executing Python: {e}')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        obj = CodeInterpreter.objects.get(pk=object_id)
        
        if obj.result:
            # Convert the string result back to a list of tuples
            results = eval(obj.result)
            extra_context['results'] = results
        
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )
    
    def response_change(self, request, obj):
        if "_run" in request.POST:
            obj.save()  # This will trigger the save method which executes the code
            # Redirect back to the change form after executing the code
            return HttpResponseRedirect(request.path)
        return super().response_change(request, obj)

        

# def execute_code(modeladmin, request, queryset):
#     for obj in queryset:
#         obj.save()  # This will trigger the save method which executes the code

# execute_code.short_description = "Execute selected code"





admin.site.register(AffiliateApp)
admin.site.register(LocationType)
admin.site.register(Tag)
