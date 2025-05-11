#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    numbers = 10
    while numbers > 0:
        print(numbers)
        numbers -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    squares = [num * num for num in int_list]
    print(squares)
    return squares

    pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass

fizzbuzz()