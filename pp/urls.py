from django.urls import path
from . import views

app_name = "pp"
urlpatterns =[
    path("", views.index,name="index"),
    path('resume/',views.pdf_download,name="resume_download"),
]