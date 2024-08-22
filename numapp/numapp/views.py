from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

@csrf_exempt
def sum_numbers(request):
    data = json.loads(request.body)
    numbers = data.gets("numbers")
    result = sum(numbers)
    return JsonResponse(
        {'foo', 'bar'}   
    )

# def average_numbers(request):
#     data = json.loads(request.body)
#     numbers = data.gets("numbers")
#     return JsonResponse(
#         {'foo', 'bar'}   
#     )

# def product_numbers(request):
#     data = json.loads(request.body)
#     numbers = data.gets("numbers")
#     return JsonResponse(
#         {'foo', 'bar'}   
#     )

 # sum = 0
    # for key, val in data.items():
    #     if isinstance(val, int):  
    #         sum += val