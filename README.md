```markdown
# Python Code Snippets

This repository contains Python code snippets demonstrating various tasks.

## Calculating the Area of a Triangle

```python
length = 5
width = 3
area = length * width
print("The area of triangle is", area)
```

## Checking if a Number is Even or Odd

```python
num1 = int(input("Enter a number: "))
if (num1 % 2) == 0:
    print("{0} is Even".format(num1))
else:
    print("{0} is Odd".format(num1))
```

## Reversing a String

```python
s = "Maham"
reversed_s = s[::-1]
print(reversed_s)
```

## Generating Fibonacci Series

```python
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
```

## Converting Celsius to Fahrenheit

```python
C = float(input("Enter Celsius: "))
f = (C * 9/5) + 32
print("Fahrenheit:", f)
```

## Checking Leap Year

```python
year = 2020

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

## Calculating the Sum of Digits in a Number

```python
num = 12345
sum = 0
for digit in str(num):
    sum = sum + int(digit)
print("Sum of digits:", sum)
```
Advancing python(:
```
