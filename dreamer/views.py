from django.shortcuts import render, get_object_or_404
from .models import Dreamer

# Create your views here.
def index(request):
    dreamer = get_object_or_404(Dreamer)
    return render(request, 'dreamer/index.html', {'dreamer': dreamer})
