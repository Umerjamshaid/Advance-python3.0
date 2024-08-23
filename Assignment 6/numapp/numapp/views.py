from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def sum_numbers(request):
    data = json.loads(request.body)
    numbers = data.get("numbers")  # Use get instead of gets
    result = sum(numbers)
    return JsonResponse({'result': result})

@csrf_exempt
def average_numbers(request):
    data = json.loads(request.body)
    numbers = data.get("numbers")
    result = sum(numbers) / len(numbers)  # Calculate the average
    return JsonResponse({'result': result})

@csrf_exempt
def product_numbers(request):
    data = json.loads(request.body)
    numbers = data.get("numbers")
    result = 1
    for number in numbers:
        result *= number  # Calculate the product
    return JsonResponse({'result': result})
