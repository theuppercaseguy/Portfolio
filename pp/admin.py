from django.contrib import admin
from .models import Reviewsss
# Register your models here.

class Reviewsss_admin(admin.ModelAdmin):
    list_display = (
        'id','review','name',
    )


admin.site.register(Reviewsss,Reviewsss_admin)