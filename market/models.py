from django.db import models

from django.utils.translation import gettext_lazy as _

BOOK_COVERS = (('hard', 'hard'), ('soft', 'soft'), ('spec', 'spec'),)


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
    authors = models.ManyToManyField(Author, related_name="books", verbose_name=_("Authors"))
    categories = models.ManyToManyField(Category, related_name="books", verbose_name=_("Categories"))
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    page_count = models.IntegerField(verbose_name=_("Page count"))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name=_("Image"))
    cover = models.CharField(choices=BOOK_COVERS, max_length=4, default="soft", verbose_name=_("Cover"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
