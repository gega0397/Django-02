from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from market.models import Book
from market.serializers import BookSerializer


# serialize("json", SomeModel.objects.all(), cls=LazyEncoder)

def get_all(request):
    books = Book.objects.all()

    if books.exists():
        books_serializer = BookSerializer(books, many=True).data
        return HttpResponse(books_serializer, content_type="text/json-comment-filtered")
    else:
        return JsonResponse({"message": "No products found"}, status=404)


def get_one(request, product_id):
    book = Book.objects.get(id=int(product_id))

    if not book:
        return JsonResponse({"message": "No products found"},
                            status=404)

    book_serializer = BookSerializer([book], many=True)

    if book_serializer:
        book_data = book_serializer.data
        print(book_data)
        return HttpResponse(book_data, content_type="text/json-comment-filtered")


def wrong_api_request(request, product_id):
    return JsonResponse({"message": f"Param should be UInt, not {product_id}:{type(product_id)}"},
                        status=404)


def web_get_all(request):
    books = Book.objects.all()

    page = request.GET.get('page', '1')

    paginator = Paginator(books, 2)

    _page = page if page.isdigit() else '1'

    print(_page, type(_page))
    _books = paginator.get_page(_page)

    print(dir(_books))
    # print(_books.end_index())
    return render(request, 'market/books.html', {"books": _books})


def web_get_one(request, product_id):
    try:
        book = Book.objects.get(id=product_id)
    except Book.DoesNotExist as e:
        return redirect(reverse('market:web_get_all'))

    if not book:
        return redirect(reverse('market:web_get_all'))

    return render(request, 'market/book.html', {"book": book})
