from django.shortcuts import render

# Create your views here.


def become_designer(request):
    return render(request, 'designer/become_designer.html')
