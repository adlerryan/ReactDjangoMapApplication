from django.db import models

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

    # Relationships
    affiliate_apps = models.ManyToManyField(AffiliateApp, blank=True)
    location_types = models.ManyToManyField(LocationType, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class SpotImage(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='spot_images/')
    is_main_image = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.spot.name}"
