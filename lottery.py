#lottery app
#lottery numbers
#jackpot number is 30
#user enters name
#if your number matches the jackpot number then user win the prize

import random


def lottery_calc():
    lottery_paddy = input("Enter your name: ")
    lottery_numbers = int(input("enter your number: "))
    lottery_gen = random.randint(0,50)
    if lottery_gen == lottery_numbers:
       print( lottery_paddy,"congrat", lottery_numbers, "you are lucky winner")
    else:
        print( lottery_paddy,"hi player", lottery_numbers, "you lost the winning number,try again later")

       




lottery_calc()