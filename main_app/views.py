from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Treat
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches,
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.treats.all().values_list('id')
  treats_finch_doesnt_have = Treat.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {
    'finch': finch,
    'feeding_form': feeding_form,
    'treats': treats_finch_doesnt_have
  })

def assoc_treat(request, finch_id, treat_id):
  finch = Finch.objects.get(id=finch_id)
  finch.treats.add(treat_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_treat(request, finch_id, treat_id):
  Finch.objects.get(id=finch_id).treats.remove(treat_id)
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class TreatList(ListView):
  model = Treat

class TreatDetail(DetailView):
  model = Treat

class TreatCreate(CreateView):
  model = Treat
  fields = '__all__'

class TreatUpdate(UpdateView):
  model = Treat
  fields = ['name', 'color']

class TreatDelete(DeleteView):
  model = Treat
  success_url = '/treats/'