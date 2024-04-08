from django.urls import path

from market.views import get_all, get_one

BASE_PATH = 'market'

urlpatterns = [
    path(f'{BASE_PATH}', get_all, name='products'),
    path(f'{BASE_PATH}/books/<int:product_id>/', get_one, name='product')
]
