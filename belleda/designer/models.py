from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Designer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(
        User, related_name='designer', on_delete=models.CASCADE)

    # To order Designers by name
    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
