from django.forms import ModelForm

from design.models import Design


class  DesignForm(ModelForm):
    class Meta:
        model = Design
        fields = ['category', 'image', 'title',  'description', 'price']
