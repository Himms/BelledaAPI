from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect

from .forms import DesignForm
from design.models import Design

from .models import Designer
# from design.models import Design

#def frontpage(request):
#    newest_products = Designer.objects.all() [0:8]
 #   return render(request, 'frontpage.html' ,{'newest_products': newest_products})

def become_designer(request):
    # check if the form has been submitted
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            designer = Designer.objects.create(
                name=user.username, created_by=user)

            return redirect('frontpage')

    else:
        form = UserCreationForm()

    return render(request, 'become_designer.html', {'form': form})


@login_required
def designer_admin(request):
    designer = request.user.designer
    designs = designer.designs.all()

    return render(request, 'designer_admin.html', {'designer': designer, 'designs': designs})

@login_required
def add_design(request):
    if request.method == 'POST':
        form =DesignForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.designer = request.user.designer
            product.slug = slugify(product.title)
            product.save()

            return redirect('designer_admin')
    else:
        form = DesignForm()
    return render(request, 'add_design.html', {'form': form})
