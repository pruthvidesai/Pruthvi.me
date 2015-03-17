from django.shortcuts import render
from momentographer.models import Momento

# Create your views here.
def index(request):
    images = Momento.objects.all()

    return render(request, 'momentographer/index.html', {'images': images})
