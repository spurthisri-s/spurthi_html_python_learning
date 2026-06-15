# Day 4 - Functions

def greet(name):
    print("Hello,", name)

def square(number):
    return number * number

user_name = input("Enter your name: ")
greet(user_name)

num = int(input("Enter a number: "))
result = square(num)

print("Square =", result)