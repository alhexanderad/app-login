from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from movies.models import Film, Commercial
from movies.forms import MovieSelectForm, FilmModelForm, CommercialModelForm

class MovieSelectFormView(FormView):
  form_class = MovieSelectForm
  template_name = 'movies/main.html'
  success_url = reverse_lazy('movies:add-movie-view')
  
  def post(self, *args, **kwargs):
    self.request.session['movie'] = self.request.POST.get('movie').lower().capitalize()
    print(self.request.POST.get('movie').lower().capitalize())
    return super().post(*args, **kwargs)

class AddMovieFormView(FormView):
  template_name = 'movies/add.html'
  success_url = reverse_lazy('home')

  def get_form_class(self, *args, **kwargs):
    movie = self.request.session.get('movie')
    print(movie)
    if movie == 'Film':
      return FilmModelForm
    else:
      return CommercialModelForm
  
  def form_valid(self, form):
    print('Seesta grabando')
    form.save()
    return super().form_valid(form)