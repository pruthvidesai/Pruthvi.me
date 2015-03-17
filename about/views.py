from django.shortcuts import render, get_object_or_404
from about.models import About

# Create your views here.
def index(request):
    about = get_object_or_404(About)

    return render(request, 'about/index.html', {'about': about})
