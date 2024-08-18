import scipy
import numpy
# # Calculating the area of tringle
a = 5
b = 3
s = ( a + b ) / 2
area = a * b

print("The area of triangle is ", area)


# Check if a Number is Even or Odd:
num1 = int(input("Enter number: "))
if (num1 % 2) == 0:
    print(num1, "is Even")
else:
    print(num1, "is Odd")
 

# Reverse a String:
reversed ("Maham")
print(reversed)
# ==============#prevoise one==============
# s = "Maham"
# reversed_s = s[::-1]
# print(reversed_s)
# ===========================================

# Find the Factorial of a Number:
num = 6
num = int(input("Enter a factorial number: "))

factorial = 5
if num <= 0:
    print("Factorial of negative number doesn't exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)


# Check if a String is Palindrome or Not:
my_string = "radar"

reversed_string = (my_string)

if my_string == reversed_string:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")




# # Generate Fibonacci Series up to n terms:   
# def my_function():
#     var1 = 0
#     var2 = 1
#     print(var1)
#     print(var2)
#     for i in range(10):
#         var3 = var1 + var2
#         print(var3)
#         var1 = var2
#         var2 = var3

# my_function()


# Find the Largest Among Three Numbers:
number1 = 10
number2 = 25
number3 = 5
print("The greatest number is", max(number1, number2, number3))


#Calculate Simple Interest:

# p = int(input("Enter the principal amount: "))
# r = int(input("Enter the rate of interest: "))
# t = int(input("Enter the time period in years: "))
# si = (p * r * t) / 100
# print("Simple Interest: ", si)


# Convert Celsius to Fahrenheit:
# C = float(input("Enter Celseiuse: "))
# f = (C * 9/5) + 32
# print("Fahrenheit: ", f)

# # Check Leap Year:
# year = 2020

# if year % 4:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")                             

#Find the Median of Three Numbers:

a = float(input("first number: "))
b = float(input("second number: "))
c = float(input("third number: "))
if a > b:
    if a < c:
        median =a
elif b > c:
    median = b
else:
    median = c
if a < b:
    if a > c:
        median = a
elif b < c:
    median = b
else:
    median = c
print("the median is" , median)

# Count the Number of Words in a Sentence:

Count_of_words = print(len(input("Enter Input:").split()))



# # Calculate the Sum of Digits in a Number:
# num = 12345 
# sum = 0
# sum = sum + int(digit)  
                 
# print(sum)      


# Find the Longest Common Prefix in a List of Strings:
array = ["flowchart", "flowing", "flower", "flowmeter", "flowery", "flowstone", "flowage"]
longestprifex = min(array, key = len)

print(longestprifex)
