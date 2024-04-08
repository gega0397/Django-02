from django.http import HttpResponse, JsonResponse

from market.models import Book, BookSerializer


# serialize("json", SomeModel.objects.all(), cls=LazyEncoder)

def get_all(request):
    books = Book.objects.all()

    if books.exists():
        books_serializer = BookSerializer(books, many=True).data
        return HttpResponse(books_serializer, content_type="text/json-comment-filtered")
    else:
        return JsonResponse({"message": "No products found"}, status=404)


def get_one(request, product_id):
    print(product_id)
    book = Book.objects.get(id=product_id)

    book_serializer = BookSerializer([book], many=True)

    if book_serializer:
        book_data = book_serializer.data
        print(book_data)
        return HttpResponse(book_data, content_type="text/json-comment-filtered")
    return JsonResponse({"message": "No products found"},
                        status=404)
