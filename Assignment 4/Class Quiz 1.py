# Question: You have a list of strings ['apple', 'banana', 'cherry', 'date', 'elderberry']. Use the filter function and a lambda function to create a new list that contains only the strings with more than 5 characters.

# Input: ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Expected Output: ['banana', 'cherry', 'elderberry']


list_ = ['apple', 'banana', 'cherry', 'date', 'elderberry']
new_list = list(filter(lambda list: len(list) > 5, list_))

print(new_list)


# Question: Given a list of numbers [2, 4, 6, 8, 10], first use the map function and a lambda function to double each number. Then, use the reduce function to find the product of the doubled numbers.

# Input: [2, 4, 6, 8, 10]
# Expected Output: 122880 (Product of [4, 8, 12, 16, 20])

from functools import reduce


list_ = [2, 4, 6, 8, 10]
num_list = list (map(lambda x: x*2, list_))

print(num_list)



product_list = reduce(lambda x, y: x*y, num_list, 1)

print( "here is the product of the numbers" , product_list)
