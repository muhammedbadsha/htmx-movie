import json
from django.views.decorators.http import require_POST
from django.shortcuts import render,redirect,HttpResponse
from .forms import MovieForm
from .models import Movie
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def movie_list(request):
    return render(request, 'movie_list.html', {
        'movies': Movie.objects.all(),
    })

def add_movie(request):
    if request.method == 'POST':
        forms = MovieForm(request.POST)
        if forms.is_valid():
            movie = forms.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{movie.title} added."
                    })
                })
    else:
        forms = MovieForm(request.POST)

    return render(request,'movie_forms.html',{'form':forms})


def edit_movie(request,pk, template_name='movie_forms.html'):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        forms = MovieForm(request.POST,instance=movie)
        if forms.is_valid():
            forms.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{movie.title} updated."
                    })
                }
            )
    else:
        forms = MovieForm(instance = movie)

    return render(request, template_name,{'form':forms,'movie':movie})
        

@ require_POST
def remove_movie(request,pk):
    movie = Movie.objects.get(pk = pk)
    movie.delete()
    
    return HttpResponse(status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{movie.title} deleted."
                    })
                })  