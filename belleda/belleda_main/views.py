from django.shortcuts import render

# Create your views here.


# def base(request):
#     return render(request, 'base.html')


def frontpage(request):
    return render(request, 'frontpage.html')


def nav_item(request):
    return render(request, 'nav_item.html')
