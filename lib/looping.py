#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    # Write a function happy_new_year() using a while loop 
    # that outputs numbers starting at 10 and counting down to 1. After reaching 1, print out "Happy New Year!"
    # pass
    num=10
    while num>0:
       
       print(num)
       num-=1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    result=[i*i for i in int_list]
    return result

def fizzbuzz():
    # code goes here!
    num=1
    while num <=100:
        if num%3==0 and num%5==0:
            print('FizzBuzz')
        elif num%3==0:
            print('Fizz')
        elif num%5==0:
            print('Buzz')
        else:
            print(num)
        num+=1
