# CS 303E Mock Exam 2
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1 - Student Class
# DO NOT CHANGE ANYTHING IN THE COURSE CLASS
class Course:
    """A course with a name, professor, and number of credit hours"""
    def __init__(self, name, professor, hours):
        """Create a new course with the given name (a string), professor (a string), and hours (an integer)"""
        self.__name = name
        self.__professor = professor
        self.__hours = hours
    
    def getName(self):
        """Returns the name of this course"""
        return self.__name
    
    def getProfessor(self):
        """Returns the professor for this course"""
        return self.__professor
    
    def getHours(self):
        """Returns the number of credit hours this course counts for"""
        return self.__hours
    
    def __str__(self):
        """Returns the string representation of this course"""
        return "{} with {}".format(self.__name, self.__professor)

# Complete the Student class below
class Student:
    def __init__(self, name, year, major, courses):
        # replace pass with your __init__ implementation here
        self.__name = name 
        self.__year = year 
        self.__major = major 
        self.__numCourses = len(courses)
        self.__courses = courses
        self.__totalHours = 0
        if self.__year == 1:
            self.__yyear = 'freshman'
        elif self.__year == 2:
            self.__yyear = 'sophomore'
        elif self.__year == 3:
            self.__yyear = 'junior'
        elif self.__year == 4: 
            self.__yyear = 'senior'
        
        

    def numCourses(self):
        # replace pass with your numCourses implementation here
        return self.__numCourses
        

    def isUpperClassman(self):
        # replace pass with your isUpperClassman implementation here
        if self.__year >= 3:
            return True
        else:
            return False

        
    def totalHours(self):
        # replace pass with your totalHours implementation here
        total = 0 
        for i in range (len(self.__courses)):
            total += self.__courses[i].getHours()
        return total
        

    def __str__(self):
        # replace pass with your __str__ implementation here
        return self.__name + ' is a ' + self.__yyear +' ' + self.__major + ' major.'
        
        


# Problem 2 - ASCII List to String
def asciiListToString(lst):
    # replace pass with your solution to problem 2 here
    out = ''
    for i in range (len(lst)):
        out += chr(lst[i])
    return out 
        
    pass


# Problem 3 - Essay Character Count
def essayCharacterCount(sentence, words):
    # replace pass with your solution to problem 3 here
    '''
    sentence = sentence.lower()
    for word in words:
        word = word.lower()
    
    listSentence = sentence.split()
    dontCount = list(words)
    sub = [a for a in listSentence]
    out = ''
    for a in dontCount:
        if a in listSentence:
            sub.remove(a)
    for x in sub:
        out += x
    print(out)
    return len(out)
    
    '''
    dontcount = list(words)
    
    sentence = sentence.lower()
    
    for thing in dontcount:
        sentence = sentence.replace(" " + thing +" ", ' ')
        if sentence.find(thing) == 0:
            sentence = sentence.replace(thing + " ", '')
        if sentence.find(thing) == len(sentence) -(len(thing)):
            sentence = sentence.replace(" " + thing, '')
        if sentence.find(thing) == 0 and sentence.find(thing) == len(sentence) -(len(thing)):
          sentence = sentence.replace(thing, '')

    
    return len(sentence.replace(" ",""))
    

# Problem 4 - Dueling Tanks
def duelingTanks(grid):
    totalduel = 0
    # replace pass with your solution to problem 4 here
    for row in grid:
        tanks = 0
        for thing in row:
            if thing == "T":
                tanks += 1
        if tanks > 0: 
            totalduel += (tanks-1)
        

    for k in range(len(grid[0])):
        tanks = 0
        for thing in grid:
          if (thing[k] == "T"):
              tanks += 1
        if tanks > 0: 
            totalduel += (tanks-1)

    return(totalduel)


# Problem 5 - Even Elements Dictionary
def evenElementsDict(tups):
    # replace pass with your solution to problem 5 here
    
    string = []
    newdic = {}
    for x in tups:
        count = 0
        for i in range (len(x)):
            if x[i] % 2 == 0:
                count += 1
        newdic[x] = count 

    return newdic
        
        

    print(string)
                
            
    pass
    

# Problem 6 - Set of Common Factors
def setOfCommonFactors(lst):
    answer = set()
    n = set()
    new = set()
    # replace pass with your solution to problem 6 here
    if len(lst) > 1:
        for i in range (len(lst)):
            new = set()
            for j in range (1, lst[i]+1):
                if lst[i] % j == 0 and i == 0:
                    answer.add(j)
                else:
                    if lst[i] % j == 0:
                        new.add(j)
                        n = answer.intersection(new)
    
    if len(lst) > 1:
        return n 
    else:
        for j in range (1, lst[0]+1):
            if lst[0] % j == 0:
                answer.add(j)

        return answer
            
                
            
                
                
            
    
    
  


# Problem 7 - Recursive Character Last Index Dictionary
def characterLastIndexDictionary(string, index):
    
    # replace pass with your solution to problem 7 here
    
    index += 1
    if len(string) < index:
        return{}
    answer = characterLastIndexDictionary(string, index)
    answer[string[-index]] = len(string) - index
    return answer

    
    
  
    '''
    if index == 0:
        gg = {}
        gg[string[index]] = index
        gg.update(characterLastIndexDictionary(string, index+1)) 
        return gg 
        
        
    if index > 0 and index < len(string):
        #{string[index]:index}.update((characterLastIndexDictionary(string, index+1)))
        return {string[index]:index}

----------------------------------
    
        if index == 0:
        gg = {string[index]:index}
    if index > 0 and index < len(string):
        return ({string[index]:index})

    return gg.update(characterLastIndexDictionary(string, index+1))
    
    if index < len(string):
        if index == 0:
            answer = {}
        answer[string[index]] = index
        return characterLastIndexDictionary(string.replace(string[index],"",1), index + 1)

    return answer
        
    '''

# Problem 8 - Recursive Divisible by 3 and 5
def divBy3And5(lst):
    # replace pass with your solution to problem 8 here
    if len(lst) == 0:
        return (0 , 0)
    else:
        if lst[0] % 3 == 0 and lst[0] %5 == 0:
            return (1 + divBy3And5(lst[1:])[0] , 1 + divBy3And5(lst[1:])[1])  
        if lst[0] % 3 == 0 and lst[0] %5 != 0:
            return (1 + divBy3And5(lst[1:])[0] , 0 + divBy3And5(lst[1:])[1]) 
        if lst[0] % 3 != 0 and lst[0] %5 == 0:
            return (0 + divBy3And5(lst[1:])[0] , 1 + divBy3And5(lst[1:])[1]) 
        
    return (0 + divBy3And5(lst[1:])[0], 0+ divBy3And5(lst[1:])[1])
    
    
    pass


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases

    # s = Student('Candice', 1, 'Chemistry', [Course('CH 301', 'Laude', 3), \
    #     Course('CS 303E', 'Young', 3), Course('UGS 303', 'Murry', 3), \
    #     Course('M 408C', 'Davis', 4), Course('GOV 310L', 'Moser', 3)])
    # print(s.isUpperClassman())
    # print(s.numCourses())
    # print(s.totalHours())
    # print(str(s))

    # print(asciiListToString([72, 101, 108, 108, 111]))
    # print(asciiListToString([]))
    # print(asciiListToString([123, 116, 114, 51, 51, 32, 37, 33, 125]))

    # print(essayCharacterCount('In conclusion the United States of America is a country', \
    #     {'the', 'a', 'an', 'at', 'but', 'by', 'in', 'for', 'of', 'on', 'to'}))
    # print(essayCharacterCount('Ultimately we shall see that history is not my strongest subject', \
    #     {'this', 'that', 'these', 'those', 'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', \
    #     'him', 'her', 'us', 'them', 'my', 'his', 'hers'}))
    # print(essayCharacterCount('nOne Of thiS actually cOuntS', {'words', 'actually', 'are', \
    #     'none', 'of', 'your', 'business', 'this', 'counts', 'as', 'poetry'}))

    # print(duelingTanks([['T', '.', '.', 'T', '.', 'T'], ['T', 'T', '.', '.', '.', '.'], \
    #     ['.', '.', 'T', 'T', '.', 'T'], ['.', 'T', '.', '.', '.', '.'], ['T', '.', '.', 'T', '.', '.']]))
    # print(duelingTanks([['T', '.', 'T'], ['.', 'T', '.'], ['T', '.', 'T']]))
    # print(duelingTanks([['.', '.', 'T', '.'], ['T', '.', '.', '.'], ['.', '.', '.', 'T'], ['.', 'T', '.', '.']]))

    # print(evenElementsDict({(1, 2, 3, 4, 5), (2, 222, 2), (17,)}))
    # print(evenElementsDict(set()))
    # print(evenElementsDict({(0,), (1, 3, 5, 7, 9), (3, 1, 4, 1, 5, 9), (98, 76, 54, 32, 10)}))

    # print(setOfCommonFactors([50, 100]))
    # print(setOfCommonFactors([18]))
    # print(setOfCommonFactors([210, 770, 2730, 1015]))

    # print(characterLastIndexDictionary('Hello World!', 0))
    # print(characterLastIndexDictionary('', 0))
    # print(characterLastIndexDictionary('CS303E is fun CS303E is fun CS303E is fun', 0))

    # print(divBy3And5([15, 9, 7, 5, 3]))
    # print(divBy3And5([]))
    # print(divBy3And5([32, 47, -200, 5, 20]))


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT