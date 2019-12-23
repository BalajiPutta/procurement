from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(Product_details)
admin.site.register(User_details)
admin.site.register(StatusType)
admin.site.register(VendorDetails)
admin.site.register(ProcurementRequest)

admin.site.register(ProcurementFulfillment)