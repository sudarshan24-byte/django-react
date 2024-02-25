from django.contrib import admin
from .models import Car

# Register your models here.
@admin.register(Car)
class UserAdmin(admin.ModelAdmin):
    list_display = ('company', 'model', 'price', 'top_speed', 'hp')

    # def body_preview(self, obj):
    #     return obj.body[:50] if len(obj.body) > 50 else obj.body