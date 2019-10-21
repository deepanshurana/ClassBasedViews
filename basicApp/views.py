from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from basicApp.models import School, Student
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView)
# Create your views here.


class indexView(TemplateView):

    template_name = 'basicApp/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection'
        return context


class schoolListView(ListView):
    model = School
    context_object_name = 'schools'
    template_name = 'basicApp/schoolList.html'


class schoolDetailView(DetailView):
    context_object_name = 'schoolDetails'
    model = School
    template_name = 'basicApp/schoolDetail.html'


class schoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = School


class schoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = School
