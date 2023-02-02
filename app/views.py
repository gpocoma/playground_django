from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from api.models import Estudiante
from django.urls import reverse_lazy


# Create your views here.


class IndexView(TemplateView):
    template_name = 'app/index.html'


class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'app/estudiante_list_view.html'


class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = '__all__'
    success_url = reverse_lazy('estudiante_list_view')
    template_name = 'app/estudiante_create_view.html'


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = '__all__'
    success_url = reverse_lazy('estudiante_list_view')
    template_name = 'app/estudiante_update_view.html'


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list_view')
    template_name = 'app/estudiante_delete_view.html'


class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'app/estudiante_detail_view.html'
