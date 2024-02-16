from django.shortcuts import render, HttpResponse, redirect

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


def valasz_view(request):
    template = 'valasz.html'
    if request.method=='POST':
        kerdes = request.POST['kerdes']
        valasz = request.POST['valasz']
        print(f'A felhasználó a {kerdes} kérdésre ezt válaszolta: {valasz}')
        teny = Teny.objects.filter(nev=kerdes).first() # Ha nem talál ilyet, akkor None-t ad vissza
        if teny == None:
            return HttpResponse('tudod kivel szórakozzál...')
        print(f'A felhasználó a {kerdes} kérdésére a jó válasz ez lenne: {teny.ido}')

        if valasz == str(teny.ido):
            context = {'ertekeles': 'jó'}
        else:
            context = {'ertekeles': 'rossz'}           
        return render(request, template, context)
    else:
        return redirect('kezdooldal')


    