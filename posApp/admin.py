from django.contrib import admin
from posApp.models import Category, Products, Sales, salesItems, Supplier,PurchaseMaster,PurchaseDetails,Customers

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)
admin.site.register(Supplier)
admin.site.register(PurchaseMaster)
admin.site.register(PurchaseDetails)
admin.site.register(Customers)

# admin.site.register(Employees)
