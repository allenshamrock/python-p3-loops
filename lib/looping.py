#!/usr/bin/env python3


def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num**2)
    return squared_list


def fizzbuzz(n):
    # code goes here!
    for i in range(1, n):
        if n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
      
            
 