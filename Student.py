# File: Student.py
# Student: Ting Wei Wu
# UT EID: tw28634
# Course Name: CS303E
# 
# Date: 2022/3/21
# Description of Program: This program is a class that can calculate student's exam average and create a student object.

class Student:
    def __init__(self, name, exam1 = 'None', exam2 = 'None'):
        self.__name = name 
        self.__exam1 = str(exam1)
        self.__exam2 = str(exam2) 


    def __str__(self):
        return 'Student: ' + self.__name + '\n  Exam1: ' + str(self.__exam1) + '\n  Exam2: ' + str(self.__exam2)

    def getName(self):
        print (self.__name)

    def getExam1Grade(self):
        if (self.__exam1 != 'None'):
            print(self.__exam1)

        
    def setExam1Grade(self, exam1):
        self.__exam1 = exam1
    
    def getExam2Grade(self):
        if (self.__exam2 != 'None'):
            print(self.__exam2)
    
    def setExam2Grade(self, exam2):
        self.__exam2 = exam2

    def getAverage(self): 
        if (str(self.__exam1) != 'None' and str(self.__exam2) != 'None'):
                average = ((float(self.__exam1) + float(self.__exam2))/2)
                if (average % 2 == 0):
                    print(int(average))
                else:
                    print(average)
        else:
            print('Some exam grades not available.')
            