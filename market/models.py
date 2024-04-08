from django.db import models
from rest_framework import serializers

from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    surname = models.CharField(max_length=100, verbose_name=_("Surname"))
    birth_date = models.DateField(verbose_name=_("Birth date"))

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Category(models.Model):
    genre = models.CharField(max_length=100, verbose_name=_("Genre"))

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    page_count = models.IntegerField(verbose_name=_("Page count"))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    image = models.ImageField(upload_to='books/', blank=True, null=True, verbose_name=_("Image"))
    authors = models.ManyToManyField(Author, verbose_name=_("Authors"))
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'birth_date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'genre']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'page_count', 'price', 'image', 'authors', 'categories']
