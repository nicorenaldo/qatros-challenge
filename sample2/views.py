from django.shortcuts import render
from django.views.generic.base import TemplateView, View

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.template.loader import render_to_string
# from .serializers import ItemsSerializer
from .models import Bus,Schedule,Station
from .forms import BusForm, ScheduleForm, StationForm
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def documentation(request):
    template = 'sample2/documentation.html'
    return render(request, template)

def index (request):
    bus = Bus.objects.all()
    schedule = Schedule.objects.all()

    search_query= request.GET.get('qq')
    if search_query :
        schedule = schedule.filter(
            Q(day__icontains = search_query)|
            Q(bus__name__icontains = search_query)|
            Q(origin__name__icontains = search_query)|
            Q(destination__name__icontains = search_query)|
            Q(code__icontains = search_query)
        )

    if request.is_ajax():
        html = render_to_string(
            template_name="sample2/result-partial.html", 
            context={"schedule": schedule}
        )
        data_dict = {"html_from_view2": html}
        return JsonResponse(data=data_dict, safe=False)
        
    template = 'sample2/index.html'

    context = {'bus' : bus, 'schedule':schedule}
    return render(request, template , context)

def BusCreate(request):
    form = BusForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context = {'form': form}
    return render(request, 'sample/submit.html', context)

def ScheduleCreate(request):
    form = ScheduleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context = {'form': form}
    return render(request, 'sample/submit.html', context)

def StationCreate(request):
    form = StationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context = {'form': form}
    return render(request, 'sample/submit.html', context)

class BusDetailViews(DetailView):
    model = Bus
    template_name = 'sample2/detail_bus.html'  
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(BusDetailViews, self).get_context_data(**kwargs)
        our_bus = get_object_or_404(Bus, pk=self.kwargs.get('pk'))
        all_schedule = our_bus.schedule_set.all()
        context["detail"] = self.object
        context["all_schedule"] = all_schedule
        return context

class ScheduleDetailViews(DetailView):
    model = Schedule
    template_name = 'sample2/detail_schedule.html'  
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ScheduleDetailViews, self).get_context_data(**kwargs)
        context["detail"] = self.object
        return context

class StationDetailViews(DetailView):
    model = Bus
    template_name = 'sample2/detail_station.html'  
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(StationDetailViews, self).get_context_data(**kwargs)
        context["detail"] = self.object
        return context

class BusUpdate(UpdateView):
    model = Bus
    fields = '__all__'
    template_name = 'sample/update.html'
    def test_func(self):
        return True

class BusDelete(DeleteView):
    model = Bus
    success_url = '/'
    def test_func(self):
        return True

class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = '__all__'
    template_name = 'sample/update.html'
    def test_func(self):
        return True

class ScheduleDelete(DeleteView):
    model = Schedule
    success_url = '/'
    def test_func(self):
        return True

class StationUpdate(UpdateView):
    model = Station
    fields = '__all__'
    template_name = 'sample/update.html'
    def test_func(self):
        return True

class StationDelete(DeleteView):
    model = Station
    success_url = '/'
    def test_func(self):
        return True