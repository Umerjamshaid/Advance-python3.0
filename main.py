# import scipy
# # Calculating the area of tringle
length = 5
width = 3
area = length * width

area = length * width 
print("The area of triangle is ", area)


# Check if a Number is Even or Odd:

num1 = int(input("Enter a number: "))
if (num1 % 2) == 0:
    print("{0} is Even".format(num1))
else:
    print("{0} is Odd".format(num1))

# Reverse a String:
s = "Maham"
reversed_s = s[::-1]
print(reversed_s)

# Generate Fibonacci Series up to n terms:   
def my_function():
    var1 = 0
    var2 = 1
    print(var1)
    print(var2)
    for i in range(10):
        var3 = var1 + var2
        print(var3)
        var1 = var2
        var2 = var3

my_function()

# Convert Celsius to Fahrenheit:
C = float(input("Enter Celseiuse: "))
f = (C * 9/5) + 32
print("Fahrenheit: ", f)

# Check Leap Year:
year = 2020

if year % 4:
    print("Leap Year")
else:
    print("Not a Leap Year")


# Calculate the Sum of Digits in a Number:
num = 12345 
sum = 0
sum = sum + int(digit)  
                 
print(sum)                                   

