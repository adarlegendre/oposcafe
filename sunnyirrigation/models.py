from django.db import models

class System_info(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    photo = models.FileField(upload_to='documents/sunnyirrigation/logo')
    location = models.CharField(max_length=200)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "System Information"

class Customers(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    profile_photo = models.FileField(upload_to='documents/sunnyirrigation/profiles')
    location = models.CharField(max_length=200)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Customers"

class Landscape(models.Model):
    name = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    climate= models.CharField(max_length=50)
    county= models.CharField(max_length=50)
    aerial_photo = models.FileField(upload_to='documents/sunnyirrigation/landscape')
    sideeast_photo = models.FileField(upload_to='documents/sunnyirrigation/landscape')
    sidewest_photo = models.FileField(upload_to='documents/sunnyirrigation/landscape')
    sidenorth_photo = models.FileField(upload_to='documents/sunnyirrigation/landscape')
    sidesouth_photo = models.FileField(upload_to='documents/sunnyirrigation/landscape')
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Landscape"


class Stations(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Stations"

class Planning(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    photo = models.FileField(upload_to='documents/sunnyirrigation/logo')
    location = models.CharField(max_length=200)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Planning"

class Devices(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    station = models.CharField(max_length=50)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Devices"

        