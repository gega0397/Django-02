from django.contrib import admin
from market.models import Book,Author,Category


# Register your models here.


# admin.site.register(Product)

@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'page_count', 'price', 'display_authors', 'display_categories')

    def display_authors(self, obj):
        return ', '.join([author.name + ' ' + author.surname for author in obj.authors.all()])
    display_authors.short_description = 'Authors'

    def display_categories(self, obj):
        return ', '.join([category.genre for category in obj.categories.all()])
    display_categories.short_description = 'Categories'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birth_date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('genre',)