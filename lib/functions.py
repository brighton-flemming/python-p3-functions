#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name="Buddy"):
    print(f"Hello, {name}!")
greet("Mario")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

def add(num1, num2):
     sum = int(num1 + num2)
     return(sum)
add(45, 55)



def halve(number):
    div = number/2
    return(float(div))
halve(99)