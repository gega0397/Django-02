from django.urls import path, re_path
from django.views.generic import RedirectView

from market.views import get_all, get_one, wrong_api_request, web_get_one, web_get_all

BASE_PATH = 'market'
wrong_api_url = r'api/books/(?P<product_id>\w+)/$'

# urlpatterns = [
#     path(f'{BASE_PATH}/api/inedx', get_all, name='products'),
#     path(f'{BASE_PATH}/api/books/<int:product_id>', get_one, name='product'),
#     re_path(wrong_api_url, wrong_api_request, name='wrong_api'),
#     path(f'{BASE_PATH}/index/', web_get_all, name='web_get_all'),
#     path(f'{BASE_PATH}/books/<int:page>', web_get_one, name='web_get_one'),
#     #re_path(r'^.*$', RedirectView.as_view(pattern_name='web_get_all')),
# ]

app_name = 'market'

urlpatterns = [
    path(f'api/', get_all, name='products'),
    path(f'api/books/<int:product_id>', get_one, name='product'),
    re_path(wrong_api_url, wrong_api_request, name='wrong_api'),
    path(f'', web_get_all, name='web_get_all'),
    path(f'books/<int:product_id>', web_get_one, name='web_get_one'),
    #re_path(r'^.*$', RedirectView.as_view(pattern_name='web_get_all')),
]
