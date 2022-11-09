from django.contrib import admin
from .models import Reviewsss,LetsTalk

# Register your models here.
class Reviewsss_admin(admin.ModelAdmin):
    list_display = (
        'id','name','title','review','linkedin','priority','turnonn',
    )

class LetsTalk_Admin(admin.ModelAdmin):
    list_display = (
        'name','company_name','company_email','message',
    )

admin.site.register(Reviewsss,Reviewsss_admin)
admin.site.register(LetsTalk,LetsTalk_Admin)