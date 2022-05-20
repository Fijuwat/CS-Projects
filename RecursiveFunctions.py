# File: RecursiveFunctions.py
# Student: Ting Wei Wu
# UT EID: tw28634
# Course Name: CS303E
# 
# Date: 04/21/2022
# Description of Program: Some recursion functions to address different problems
def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in 
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
    """ Add up the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
    if n == 0:
        return 0
    else:
        return n + addToN (n-1) 
        # return n in this round and add the n at the second round 
        

def findSumOfDigits( n ):
    """ Return the sum of the digits in a non-negative integer. """
    if n == 0:
        return 0
    else:
        return n % 10 + findSumOfDigits(n//10) 
        # return n in this round and take out the last digit to next round

def integerToBinary( n ):
    """ Given a nonnegative decimal integer n, return the 
    binary representation as a string. """
    if n <= 1:
        return str(n)
    else:
        return str(integerToBinary(n // 2)) + str(integerToBinary(n % 2)) 
        # find quotient's Remainder as the first binary and then repeat and put it into a string
    

        
def integerToList( n ):
    """ Given a nonnegative decimal integer, return a list of the 
    digits (as strings). """
    
    if len(str(n)) == 1:
        return [str(n)] 
    else:
        return (integerToList(n//10)) + [str(n%10)] 
        #return the last digit at this round and then put the everything other than the last digit in the next round. 
        
        
    

def isPalindrome( s ):
    """ Return True if string s is a palindrome and False
    otherwise. Count the empty string as a palindrome. """
    if len(s) < 2:
        return True
    if s[0] != s[-1]: 
        return False
    return isPalindrome(s[1:-1]) 
    # return true is the first and the last letter is the same letter, then take out the first and the last letter and repeat it to the next round
    

def findFirstUppercase( s ):
    """ Return the first uppercase letter in 
    string s, if any.  Return None if there
    is none. """ 
    if len(s) == 0:
        return None
    if ord(s[0]) <= 90 and ord(s[0]) >= 65 :
        return s[0]
    else:
        return findFirstUppercase( s[1:] ) 
    # return the letter immediatly if the letter examining right now is a capital letter and if not take out the first letter and put it into the next round

def findFirstUppercaseIndexHelper( s, index ):
    """ Helper function for findFirstUppercaseIndex.
    Return the index of the first uppercase letter, 
    beginning at index.  Return -1 if there is none."""
    if len(s) == 0:
        return -1
    if ord(s[index]) <= 90 and ord(s[index]) >= 65 and index < len(s) :
        return index
    else:
        if index < len(s) -1:
            return findFirstUppercaseIndexHelper( s, index+1 )
        else:
            return -1
    # if the length is equal to 0 then return -1 and if find the current letter capital letter, return its indext. if not find it capital put the next letter of string s into the function and repeat it and if it goes through everything then return -1

# The following function is already completed for you.  But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
    """ Return the index of the first uppercase letter in 
    string s, if any.  Return -1 if there is none.  This one 
    requires a helper function, which is the recursive 
    function. """
    return findFirstUppercaseIndexHelper( s, 0 )