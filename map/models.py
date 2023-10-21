from django.db import models 
import geocoder #geocoder converts physical addresses into coordinates

# Mapbox access key
access_token='pk.eyJ1IjoiYXJpZWxiMSIsImEiOiJjbGIxbnFyNW4wNXVjM3dueW5lbGVoeDRnIn0.8_79cvoMd9lBAUQKUe27tA'
# Model for grocery stores that store the address, lat, and long
class GroceryStoreAddresses(models.Model):
    address=models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

# Model for Farmers Markets that store the address, lat, and long
class FarmersMarketAddresses(models.Model):
    farmer_address=models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

    # Save function that converts physical addresses into coordinates and saves it
    def save(self, *args, **kwargs):
        g=geocoder.mapbox(self.farmer_address,key=access_token)
        g=g.latlng
        self.lat=g[0]
        self.long=g[1]
        super(FarmersMarketAddresses,self).save(*args,**kwargs)

# Model for Fire Houses that store the address, lat, and long
class FireHouseAddresses(models.Model):
    fire_address=models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

# Model for Super Markets that store the address, lat, and long
class SuperMarketAddresses(models.Model):
    supermarket_address = models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

# Model for Super Centers that store the address, lat, and long
class SupercenterAddresses(models.Model):
    supercenter_address = models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

