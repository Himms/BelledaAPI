from django.contrib import admin

# Register your models here.

from .models import Category, Design


admin.site.register(Category)
admin.site.register(Design)