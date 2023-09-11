from django.db import models
from django.db import connection


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class AffiliateApp(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class LocationType(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Spot(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    website = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    cover_charge = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    location_types = models.ManyToManyField(LocationType, blank=True, related_name='spots')
    tags = models.ManyToManyField(Tag, blank=True, related_name='spots')

    monday_open = models.TimeField(blank=True, null=True)
    monday_close = models.TimeField(blank=True, null=True)

    tuesday_open = models.TimeField(blank=True, null=True)
    tuesday_close = models.TimeField(blank=True, null=True)

    wednesday_open = models.TimeField(blank=True, null=True)
    wednesday_close = models.TimeField(blank=True, null=True)

    thursday_open = models.TimeField(blank=True, null=True)
    thursday_close = models.TimeField(blank=True, null=True)

    friday_open = models.TimeField(blank=True, null=True)
    friday_close = models.TimeField(blank=True, null=True)

    saturday_open = models.TimeField(blank=True, null=True)
    saturday_close = models.TimeField(blank=True, null=True)

    sunday_open = models.TimeField(blank=True, null=True)
    sunday_close = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class SpotAffiliate(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    affiliate_app = models.ForeignKey(AffiliateApp, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = ('spot', 'affiliate_app')

class SpotImage(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='spot_images/')
    is_main_image = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.spot.name}"
    

class MenuItem(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.item_name


# Code Interpreter to view data
class CodeInterpreter(models.Model):
    LANGUAGE_CHOICES = [
        ('SQL', 'SQL'),
        ('Python', 'Python')
    ]

    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    table = models.CharField(max_length=255)
    code = models.TextField()
    result = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.language == 'SQL':
            # Execute SQL code
            with connection.cursor() as cursor:
                cursor.execute(self.code)
                column_headers = [col[0] for col in cursor.description]
                results = cursor.fetchall()
            self.result = str((column_headers, results))
        elif self.language == 'Python':
            # Execute Python code (with some safety checks)
            self.result = str(exec(self.code))
        super().save(*args, **kwargs)

    def run_code(self):
        # Here, you'll want to have the logic that executes the code
        # For example:
        if self.language == "SQL":
            # Execute SQL code and update the result attribute
            with connection.cursor() as cursor:
                cursor.execute(self.code)
                self.result = cursor.fetchall()
        elif self.language == "Python":
            # Execute Python code and update the result attribute
            # Be very careful with this, as executing arbitrary Python code can be dangerous
            self.result = str(eval(self.code))
        self.save()
