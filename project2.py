# File: Project2.py
# Student: Ting Wei Wu
# UT EID: tw28634
# Course Name: CS303E
# 
# Date: 2022/04/10
# Description of Program: A program for different uses in The Fibonnaci Numbers
def firstNFibNumbers (n):
    """ Return a list of the first n Fibonnaci numbers.  If 
        n < 0, return the empty list. """
    
    if n <= 0:
        return []

    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1:
        return [ 0 ]
    elif n == 2:
        return [ 0, 1 ]

    # Here we know that n is at least 2.
    else:

        # Initialize fib1 and fib2 with the first 
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1
        
        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [ 0, 1 ]
        
        # Use the previous two values to generate 
        # and record the next value.
        for counter in range( 2, n ):

            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2

            # Add the newest value to the list we're
            # creating.
            fibs.append( fib2 )

        return fibs

print('')
print('Welcome to the Fibonnaci Number laboratory!')
print('')
print('The following commands are available:')
print('  0: Exit.')
print('  1: List the first N Fibonnaci numbers.')
print('  2: Display the ith Fibonnaci number (0-based).')
print('  3: List the Fibonnaci numbers less or equal to N.')
print('  4: How many Fibonnaci numbers are less or equal to N?')
print('  5: Find a list of the largest Fibonnaci numbers that add up to N.')
print('  6: Display this help message. ')

while (True):
    yesorno = True
    print('')
    answer = int(input('Please enter a command (0, 1, 2, 3, 4, 5 or 6): '))
    if (answer < 0 or answer > 6):
        print('ERROR: Illegal value entered.')
        
    if (answer == 0):
        print('')
        print('Thanks for using the Fibonnaci Laboratory!  Goodbye.')
        print()
        break

    while (answer == 1 and yesorno == True):
        answer1 = int(input('You\'ve asked for the first N Fibonnaci numbers. What is N? '))
        
        if (answer1 < 0):
            print('ERROR: Illegal value entered.')
            yesorno = False
        else:
            print(firstNFibNumbers (answer1))
            yesorno = False

    while (answer == 2 and yesorno == True):
        answer2 = int(input('You\'ve asked for the ith Fibonnaci number. What is i? '))

        if (answer2 < 0):
            print('ERROR: Illegal value entered.')
            yesorno = False
        else:
            list = firstNFibNumbers (answer2+1)
            print (list[answer2])
            yesorno = False

    while (answer == 3 and yesorno == True):
        answer3 = int(input('You\'ve asked for the Fibonnaci numbers less than or equal to N. What is N? '))
        

        if True:
            listneed = firstNFibNumbers (answer3+100) 
            newlist = []
            for i in range (answer3+100):
                if listneed[i] <= answer3: 
                    newlist.append(listneed[i])
            print(newlist)
            yesorno = False

    while (answer == 4 and yesorno == True):
        answer4 = int(input('You\'ve asked how many Fibonnaci numbers are less than or equal to N. What is N? '))

        if True:
            listneed = firstNFibNumbers (answer4+100) 
            newlist = []
            count = 0
            for i in range (answer4+100):
                if listneed[i] <= answer4: 
                    count += 1
            print(count)
            yesorno = False

    
    while (answer == 5 and yesorno == True):
        answer5 = int(input('You\'ve asked for Fibonnaci numbers that sum to N. What is N? '))
        
        if (answer5 < 0):
            print('ERROR: Illegal value entered.')
            yesorno = False
        else:
            listneed = firstNFibNumbers (answer5+5) 
            newlist2 = []
            answerlist = []
            for i in range (answer5+5):
                if listneed[i] <= answer5: 
                    newlist2.append(listneed[i])
            if answer5 == 0:
                answerlist.append(0)
                print(answerlist)
                yesorno = False
                break
            
            for x in range (-1, -1*len(newlist2), -1):
                if answer5 >= newlist2[x]:
                    answer5 -= newlist2[x]
                    answerlist.append(newlist2[x])
            
            print(answerlist)
            yesorno = False
    
    while (answer == 6 and yesorno == True):
        print('The following commands are available:')
        print('  0: Exit.')
        print('  1: List the first N Fibonnaci numbers.')
        print('  2: Display the ith Fibonnaci number (0-based).')
        print('  3: List the Fibonnaci numbers less or equal to N.')
        print('  4: How many Fibonnaci numbers are less or equal to N?')
        print('  5: Find a list of the largest Fibonnaci numbers that add up to N.')
        print('  6: Display this help message. ')        
        yesorno = False