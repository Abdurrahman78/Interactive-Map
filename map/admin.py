from django.contrib import admin 
from .models import GroceryStoreAddresses, FarmersMarketAddresses, FireHouseAddresses, SupercenterAddresses, SuperMarketAddresses

admin.site.register(GroceryStoreAddresses)
admin.site.register(FarmersMarketAddresses)
admin.site.register(FireHouseAddresses)
admin.site.register(SupercenterAddresses)
admin.site.register(SuperMarketAddresses)