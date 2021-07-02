from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Design(models.Model):
    design_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name='designs', on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    created_by = models.ForeignKey(
        'auth.User', related_name='designs', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.design_tag, self.name)


class Cart(models.Model):
    cart_id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Design)

    class Meta:
        ordering = ['cart_id', '-created_at']

    def __str__(self):
        return f'{self.cart_id}'
