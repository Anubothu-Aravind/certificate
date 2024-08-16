from django.shortcuts import render, HttpResponse
from .CertificateGeneration import *

def index(request):
    # Example usage
    certificate()
    return HttpResponse("Done")
