
from wsgiref.util import FileWrapper
from django.shortcuts import render
# from django.http import HttpResponse
from django.http.response import HttpResponse
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

import mimetypes
import os
from fpdf import FPDF


# Create your views here.
def index(request):
    return render(request, "pp/index.html")


def pdf_download(request):
    
    return FileResponse(open('Resume-Saad-Khan.pdf','rb'),as_attachment=True,content_type='application/pdf')





