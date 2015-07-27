# Main django views file for error handling
from django.shortcuts import render_to_response

def error400(reuest):
    return render_to_response('400.html')

def error403(reuest):
    return render_to_response('403.html')

def error404(request):
    return render_to_response('404.html')

def error500(request):
    return render_to_response('500.html')