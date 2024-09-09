from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def split_evenly(request):
    if request.method == 'POST':
        #The split() method is the most common way to split a string into a list in Python. This method splits a string into substrings based on a delimiter and returns a list of these substrings. myString = "Hello world" myList = myString. split() print(myList) Output: ['Hello', 'world']
        user_ids = request.POST.get('user_ids', '').split(',')  # 👈
        total_bill_amount = float(request.POST.get('total_bill_amount', 0))

        if not user_ids or total_bill_amount <= 0:
            return render(request, 'index.html', {"error": "Invalid input"})

        # Calculate the amount each user needs to pay
        num_users = len(user_ids)
                     #👆What is len() Function in Python? The len() function in Python is used to quickly determine the length or the number of items in a collection, such as a string, list, tuple, dictionary, or any other iterable object. It returns an integer representing the length of the given object.
        amount_per_user = total_bill_amount / num_users


        result = {
            'user_ids': user_ids,
            #The round function in Python is used for rounding off numbers up to a specified number of digits after the decimal point. For example, 65.234 can be rounded off to 65.2. It is an inbuilt function in Python and hence does not require any module to be imported for its usage.👇
            'amount_per_user': round(amount_per_user, 2)
        }

        return render(request, 'index.html', {'result': result})

    # Render the form for GET request
    return render(request, 'index.html')

#======================================uneven splitting=================================================
@api_view(['GET', 'POST'])
def split_unevenly(request):
    if request.method == 'POST':
        # Get form data
        user_ids = request.POST.get('user_ids', '').split(',')
        contributions = request.POST.get('contributions', '').split(',')
        total_bill_amount = float(request.POST.get('total_bill_amount', 0))

        # Convert contributions to floats
        contributions = [float(contribution) for contribution in contributions]

        # Input validation
        if not user_ids or total_bill_amount <= 0 or len(user_ids) != len(contributions):
            return render(request, 'uneven_split.html', {"error": "Invalid input"})

        # Calculate total contribution and required payment per user
        num_users = len(user_ids)
        total_contributions = sum(contributions)
        required_payment_per_user = total_bill_amount / num_users

        # Prepare result
        result = []
        #The `zip` function in Python is a built-in function that allows you to aggregate elements from multiple iterables into a single iterable. It takes two or more iterables as input and returns an iterator that produces tuples containing elements from all the input iterables.
        # ----------------------------👇
        for user_id, contribution in zip(user_ids, contributions):
            balance = round(contribution - required_payment_per_user, 2)
            result.append({
                'user_id': user_id,
                'contributed': contribution,
                'balance': balance  # Positive: overpaid, Negative: owes more
            })

        return render(request, 'uneven_split.html', {'result': result})

    # Render the form for GET request
    return render(request, 'uneven_split.html')



#======================================tax&tips splitting===========================================

@api_view(['GET', 'POST'])
def split_including_tip_tax(request):
    if request == 'POST':
        #now getting form data
        user_ids = request.POST.get("user_ids,"'').split(',')
        total_bill_amount = float(request.POST.get('total_bill_amount', 0))
        tip = float(request.POST.get('tip,', 0))
        tax = float(request.POST.get('tax,', 0))

        if not user_ids or total_bill_amount <= 0 or tip < 0 or tax < 0:
            return render(request, 'split_with_tip_tax.html', {"error": "Invalid input"})
        

        tip_amount = total_bill_amount * (tip / 100)
        tax_amount = total_bill_amount * (tax / 100)
        total_bill_amount_with_tip_and_tax = total_bill_amount + tip + tax

        num_users = len(user_ids)
        amount_per_user = total_bill_amount_with_tip_and_tax / num_users


        result = {
            'user_ids': user_ids,
            'amount_per_user': round(amount_per_user, 2)
        }

        return render(request, 'split_with_tips_tax..html', {'result': result})
    

    return render(request, 'split_with_tip_tax.html')


#======================================Handling Discounts===========================================
@api_view(['GET', 'POST'])
def handle_discounts(request):
    if request.method == 'POST':
        user_ids = request.POST.get('user_ids', '').split(',')
        total_bill_amount = float(request.POST.get('total_bill_amount',0))
        discounts_persentage = float(request.POST.get('discounts_percentage',0))

        if not user_ids or total_bill_amount <= 0:
            return render(request, 'handle_discounts.html', {"error": "Invalid input"})


        discounts_persentage = discounts_persentage / 100
        total_bill_amount_with_discound = total_bill_amount - (total_bill_amount * discounts_persentage)


        num_users = len(user_ids)
        amount_per_user = total_bill_amount_with_discound / num_users


        result = {
            'user_ids': user_ids,
            'amount_per_user': round(amount_per_user, 2)
        }

        return render(request, 'handle_discounts.html', {'result': result})
    return render(request, 'handle_discounts.html') 
    


#=========================Advanced Bill Splitting with Shared Items================================

@api_view(['GET', 'POST'])
def split_with_shared_items(request):
    if request.method == 'POST':
        user_ids = request.POST.get('user_ids', '').split(',')
        total_bill_amount = float(request.POST.get('total_bill_amount', 0))
        items_with_prices = float(request.POST.get('items_with_prices', 0))
        user_IDs_for_each_shared_item = request.POST.get('user_IDs_for_each_shared_item', '').split(',')

        if not user_ids or total_bill_amount <= 0 or items_with_prices <= 0 or len(user_ids) != len(user_IDs_for_each_shared_item):
            return render(request,'split_with_shared_ items.html', {"error": "Invalid input"})
        

        num_users = len(user_ids)
        amount_per_user = total_bill_amount / num_users
        amount_per_user_for_each_shared_item = items_with_prices / len(user_IDs_for_each_shared_item)

        result = {
            'user_ids': user_ids,
            'amount_per_user': round(amount_per_user, 2),
            'amount_per_user_for_each_shared_item': round(amount_per_user_for_each_shared_item, 2)
        }

        return render(request, 'split_with_shared_items.html', {'result': result})

    return render(request, 'split_with_shared_items.html')
