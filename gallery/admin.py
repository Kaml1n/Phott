from django.contrib import admin
from .models import Categories, Photo

class PhotoInline(admin.StackedInline):
    model=Photo
    
class ItemAdmin(admin.ModelAdmin):
    inlines=[PhotoInline]


admin.site.register(Categories, ItemAdmin)