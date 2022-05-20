# File: MinMax.py
# Student: Ting-Wei Wu
# UT EID: tw28634
# Course Name: CS303E
# 
# Date: February 25 2022
# Description of Program: This is program is created for finding the maximun and minimun of numbers.

Max = -100000000000000
Min = 1000000000000
int_stop = str(input('Enter an integer or \'stop\' to end: '))

if (int_stop == "stop"):
    print("You didn't enter any numbers")

else:
    Max = eval(int_stop)
    Min = eval(int_stop)
    while (int_stop != "stop"):
            int_stop = str(input('Enter an integer or \'stop\' to end: '))
            if (int_stop == 'stop'):
                print('The maximum is', Max)
                print('The minimum is', Min)
                break
            elif (eval(int_stop) >= Max):
                Max = eval(int_stop)
            elif (eval(int_stop) <= Min):
                Min = eval(int_stop)
                
        
        
