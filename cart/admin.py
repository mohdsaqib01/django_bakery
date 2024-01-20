from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.
class CartItemiline(admin.TabularInline):
    model = CartItem
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','created_at']
    inlines = [CartItemiline]