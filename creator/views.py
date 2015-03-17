from django.shortcuts import render, get_object_or_404
from creator.models import Creator

# Create your views here.
def index(request):
    creations = Creator.objects.filter(published=True)

    return render(request, 'creator/index.html', {'creations': creations})
