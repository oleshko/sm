# Create your views here.
from django.shortcuts import render

def sign ( request ) :
    """comment here"""
    return render( request, 'consultations/index.html', {} )

