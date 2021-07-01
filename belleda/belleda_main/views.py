from django.shortcuts import render
from design.models import Design
from designer.models import Designer

# Create your views here.


# def base(request):
#     return render(request, 'base.html')


def frontpage(request):
    newest_designs = Design.objects.all() [0:8]
    return render(request, 'frontpage.html', {'newest_designs': newest_designs})


def nav_item(request):
    return render(request, 'nav_item.html')
