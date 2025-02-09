from django.contrib import admin
from .models import Members
from . models import Product

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ('firstname', 'lastname', 'phone', 'joined_date')

admin.site.register(Members, MemberAdmin)

class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'stock', 'image_url')

admin.site.register(Product, ProductAdmin)
