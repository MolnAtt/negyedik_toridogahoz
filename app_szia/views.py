from django.shortcuts import render

from .models import Teny

from random import randint

# Create your views here.

def szia_view(request):
    template = 'index.html'
    tenyek = list(Teny.objects.all())     # list parancs kicsit túlzás, de most egyszerűsítünk
    r = randint(0, len(tenyek)-1)
    context = {
        'esemeny_neve': tenyek[r].nev,
        }
    return render(request, template, context)