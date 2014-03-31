# Create your views here.
from django.shortcuts import render

def sign ( request ) :
    
    return render( request, 'consultations/index.html', {} )