from django.shortcuts import render

from .models import Item
# Create your views here.

def productlist(request):
    queryset = Item.objects.all()

    context = {
        'queryset': queryset,
    }

    return render(request, "products.html", context)