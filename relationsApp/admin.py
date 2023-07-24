from django.contrib import admin
from .models import Profile, Account, Adress, Product

# Register your models here.
admin.site.register(Profile)
admin.site.register(Account)
admin.site.register(Adress)
admin.site.register(Product)
