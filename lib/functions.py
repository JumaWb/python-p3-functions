#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()
    

def greet(name):
    print(f"Hello, {name}!")
greet("name")
    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default("programmer")

def add(num1, num2):
    return(num1 + num2)
result=add(1,2)
print(result)

def halve(number):
    return(number/2)
result=halve(4)
print(result)
