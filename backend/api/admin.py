from django.contrib import admin
from .models import User,Category,Product

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display='__all__',
    admin.site.register(User)

class CategoryAdmin(admin.ModelAdmin):
    list_display='__all__'
    admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display='__all__'
    admin.site.register(Product)
