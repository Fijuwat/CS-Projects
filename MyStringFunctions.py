# File: MyStringFunctions.py
# Student: Ting Wei Wu
# UT EID: tw28634
# Course Name: CS303E
# 
# Date: 2022/3/26
# Description of Program: This program contains different useful string functions.

def myAppend( str, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    return str + ch
    
def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    a = 0
    for i in range (len(str)):
        if (str[i] == ch):
            a += 1
            i += 1
        else:
            i += 1
    return a
            

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1+str2
    

def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    
    if (str == ""):
        print("Empty string: no min value")
        return None
    else:
        a = str[0]
        min = ord(a)
        for i in range (len(str)):
            if (ord(str[i]) <= min):
                min = ord(str[i])
                i += 1
            else:
                i += 1
    return chr(min)
            
    
def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if (i > len(str)):
        print("Invalid index")
        return None
    else:
        return str[ : i] + ch + str [i : len(str)]
    
def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    if (i >= len(str)):
        print("Invalid index")
        return str, None
    else:
        return str[ : i] + str [i+1 : len(str)], str [i]
    
def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    if ch in str:
        for i in range (len(str)):
            if (str[i] == ch):
                return i 
            else:
                i += 1
    else:
        return -1
                
def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    if ch in str:
        find = 0
        for i in range (len(str)):
            if (str[i] == ch):
                find = i 
                i += 1
            else:
                i += 1
        return find
    else:
        return -1

def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.
    if ch in str:
        for i in range (len(str)):
            if (str[i] == ch):
                return str[:i] + str[i+1 :]  
            else:
                i += 1
    else:
        return str
            
def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    if ch in str:
        newString = ''
        for i in range (len(str)):
            if (str[i] == ch):
                continue
            else:
                newString += str[i]
                
        return newString
    else:
        return str
                

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order. 
    if (str == ''):
        return ''
    else:
        return str[:: -1]
    