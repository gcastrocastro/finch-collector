from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Finch, Sponsor
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
   finch = Finch.objects.get(id = finch_id)
   id_list = finch.sponsors.all().values_list('id')
   sponsors_finch_doesnt_have = Sponsor.objects.exclude(id__in = id_list)
   feeding_form = FeedingForm()
   return render(request, 'finches/detail.html', {
      'finch': finch,
      'feeding_form': feeding_form,
      'sponsors': sponsors_finch_doesnt_have
   })

def add_feeding(request, finch_id):
   form = FeedingForm(request.POST)
   if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.finch_id = finch_id
      new_feeding.save()
   return redirect('detail', finch_id=finch_id)

def assoc_sponsor(request, finch_id, sponsor_id):
   Finch.objects.get(id=finch_id).sponsors.add(sponsor_id)
   return redirect('detail', finch_id=finch_id)

def unassoc_sponsor(request, finch_id, sponsor_id):
   Finch.objects.get(id=finch_id).sponsors.remove(sponsor_id)
   return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
   model = Finch
   fields = ['name', 'scientific_name', 'description']

class FinchUpdate(UpdateView):
   model = Finch
   fields = ['name', 'scientific_name', 'description']

class FinchDelete(DeleteView):
   model = Finch
   fields = ['name', 'scientific_name', 'description']
   success_url = '/finches'

class SponsorCreate(CreateView):
    model = Sponsor
    fields = ['name', 'donation']

class SponsorList(ListView):
    model = Sponsor

class SponsorDetail(DetailView):
    model = Sponsor

class SponsorUpdate(UpdateView):
    model = Sponsor
    fields = ['name', 'donation']

class SponsorDelete(DeleteView):
    model = Sponsor
    success_url = '/sponsors/'