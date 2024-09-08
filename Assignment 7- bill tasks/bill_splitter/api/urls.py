from django.urls import path

from .views import split_evenly
from .views import split_unevenly
from .views import split_including_tip_tax
from .views import  handle_discounts
from .views import  split_with_shared_items
urlpatterns = [
    path('split-evenly/', split_evenly, name='split-evenly'),
    path('split-unevenly/', split_unevenly, name='split-unevenly'),
    path('split-with-tip-tax/', split_including_tip_tax, name='split_with_tip_tax'),
    path('handle-discounts/', handle_discounts, name='handle_discounts'),
    path('split-with-shared-items/', split_with_shared_items, name='split_with_shared_items'),
]
