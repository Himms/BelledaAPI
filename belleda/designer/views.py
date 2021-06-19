from django.shortcuts import render

# Create your views here.


def become_designer(request):
    return render(request, 'become_designer.html')
