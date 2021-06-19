from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Designer


def become_designer(request):
    # check if the form has been submitted
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            designer = Designer.objects.create(
                name=user.username, created_by=user)

            return redirect('base')

    return render(request, 'become_designer.html')
