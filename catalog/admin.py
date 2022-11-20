from django.contrib import admin
from .models import Category, Product, Toptext
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','availability','created','updated','stock']
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['availability','created','updated','stock']
    list_editable = ['availability','stock','price']
    search_fields = ['name','price','stock']

@admin.register(Toptext)
class ToptextAdmin(admin.ModelAdmin):
    list_display = ['name','slug','date']
    prepopulated_fields= {'slug':('name',)}
    list_filter = ['name', 'date']