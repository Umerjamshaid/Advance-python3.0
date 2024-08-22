# from django.urls import path
# from numapp import views

# urlpatterns = [
#     path('sum/', views.sum_numbers, name='sum_numbers'),
# #     path('average/', views.average_numbers, name='average_numbers'),
# #     path('product/', views.product_numbers, name='product_numbers'),
# ]


from django.urls import path
from numapp import views

urlpatterns = [
    path('api/sum/', views.sum_numbers, name='sum_numbers'),
    path('api/average/', views.average_numbers, name='average_numbers'),
    path('api/product/', views.product_numbers, name='product_numbers'),
]
