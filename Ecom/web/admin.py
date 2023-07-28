from django.contrib import admin
from . models import Product,Carosuel,Order,OrderItem
# Register your models here.
class OrderItemTubleInline(admin.TabularInline):
    model=OrderItem
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemTubleInline]
    

admin.site.register(Product)
admin.site.register(Carosuel)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)

