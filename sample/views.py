from django.views.generic.base import TemplateView, View

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.template.loader import render_to_string
from .serializers import ItemsSerializer
from .models import Items
from .forms import SubmitForm
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
    items = Items.objects.get(pk=1)
    template = 'sample/documentation.html'
    context={'items':items}
    
    return render(request, template, context)

def home(request):
    template = 'sample/home.html'
    return render(request, template)

def index (request):
    items = Items.objects.all()
    search_query= request.GET.get('q')
    if search_query :
        items = items.filter(
            Q(name__icontains = search_query)|
            Q(description__icontains = search_query)|
            Q(code__icontains = search_query)
        )
        print("cari")

    if request.is_ajax():
        html = render_to_string(
            template_name="sample/result-partial.html", 
            context={"items": items}
        )
        print(html)
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)
        
    template = 'sample/index.html'

    context = {'items' : items}
    return render(request, template , context)

class APIItems(APIView):

	def get(self,request):
		items = Items.objects.all()
		serializer = ItemsSerializer(items, many=True)
		return Response(serializer.data)

	def post(self,request, format=None):
		serializer = ItemsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def ItemCreate(request):
    form = SubmitForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, 'sample/submit.html', context)

class ItemDetailViews(DetailView):
    model = Items
    template_name = 'sample/detail.html'  
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ItemDetailViews, self).get_context_data(**kwargs)
        context["detail_product"] = self.object
        return context

class ItemUpdate(UpdateView):
    model = Items
    fields = ['name','description']
    template_name = 'sample/update.html'
    def test_func(self):
        return True

class ItemDelete(DeleteView):
    model = Items
    success_url = '/'

    def test_func(self):
        return True