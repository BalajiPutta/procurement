from django.db import models
from django.core import serializers

class Product_details(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=50,default=False)
    product_image = models.FileField(upload_to='products/media/')

data = serializers.serialize( "python", Product_details.objects.all() )


class User_details(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    contact_no = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)




class StatusType(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    update = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=50)


class VendorDetails(models.Model):
    vendor_id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    address1 = models.TextField()
    address2 = models.TextField()
    address3 = models.TextField()
    city = models.TextField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    vendor_contact_rep = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    update = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=50)


class ProcurementRequest(models.Model):
    req_id = models.AutoField(primary_key=True)
    req_title = models.CharField(max_length=100)
    req_product_id = models.ForeignKey(Product_details,on_delete=models.CASCADE)
    req_prod_quantity = models.IntegerField()
    req_due_date = models.DateField()
    req_comments = models.TextField()
    req_status = models.ForeignKey(StatusType,on_delete=models.CASCADE)
    requester_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    update = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=50)


class ProcurementFulfillment(models.Model):
    proc_ful_id = models.IntegerField(primary_key=True)
    proc_req_id = models.ForeignKey(ProcurementRequest,on_delete=models.CASCADE)
    proc_prod_id = models.ForeignKey(Product_details,on_delete=models.CASCADE)
    proc_vendor_id = models.ForeignKey(VendorDetails,on_delete=models.CASCADE)
    proc_order_date = models.DateField()
    proc_prod_order_quantity = models.IntegerField()
    req_status = models.ForeignKey(StatusType,on_delete=models.CASCADE)
    proc_ful_comments = models.TextField()
    proc_ful_cost = models.IntegerField()
    requester_id = models.IntegerField()
    req_requester_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    update = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=50)