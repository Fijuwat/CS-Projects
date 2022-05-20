# File: Project1.py
# Student: Ting-Wei Wu
# UT EID: tw28634
# Course Name: CS303E
# 
# Date: 2022/3/2
# Description of Program: This program is created for converting different english and metric unit to each other.


#variables
dash = "------------------------------------------------------------"
error = 'ERROR: Answer must be 1, 2 or 3. Try again.'
true = 2

#parameters
'''
foot = 0.3048 meters
meters = 3.28084 feet
mile = 5280 feet
inch = 1/12 feet
km = 1000 meters
cm = 1/100 meters
'''


#print intros
print()
print('Welcome to the English/Metric conversion utility.')
print()
print('This utility allows you to convert between English units \n(miles, feet, inches) and metric units (kilometers, meters, \ncentimeters).')
print()
print(dash)
print()

#First choice
while (True):
    print('Which direction would you like to convert:')
    print('   For English to Metric type: 1')
    print('   For Metric to English type: 2')
    print('   To Quit type:               3')
    print()
    eorm = str(input('   Input your answer (1, 2 or 3): '))
    print()
    true = 2
    #for answer 1
    if (eorm == '1'):
        while (true == 2):
            print('Select English units to convert to metric equivalent:')
            print('   For miles type:  1')
            print('   For feet type:   2')
            print('   For inches type: 3')
            print()
            englishU = str(input('   Choose English units to convert (1, 2 or 3): '))
            print()
            
            #for type 1 to others
            if (englishU != '1' and englishU != '2' and englishU != '3'):
                print(error)
                print()
                
            elif (englishU == '1'):
                while (true == 2):
                    print('Convert to which metric units:')
                    print('   For kilometers type:  1')
                    print('   For meters type:      2')
                    print('   For centimeters type: 3')
                    print()
                    targetm = str(input('   Choose target metric units (1, 2 or 3): '))
                    print()

                    #when enter 1
                    if (targetm == '1' and true == 2):
                        miles = float(input('Enter the number of miles to convert to kilometers: '))
                        print()
                        print('RESULT:', miles, 'miles =', '{:.3f}'.format(round(miles*5280*0.3048/1000, 3)), 'kilometers')
                        print()
                        print(dash)
                        true = 3
                        print()
                        
                    #when enter 2
                    elif (targetm == '2' and true == 2):
                        miles = float(input('Enter the number of miles to convert to meters: '))
                        print()
                        print('RESULT:', miles, 'miles =', '{:.3f}'.format(round(miles*5280*0.3048, 3), 'meters'))
                        print()
                        print(dash)
                        true = 3
                        print()

                    #when enter 3 
                    elif (targetm == '3'  and true == 2):
                        miles = float(input('Enter the number of miles to convert to centimeters: '))
                        print()
                        print('RESULT:', miles, 'miles =', '{:.3f}'.format(round(miles*5280*0.3048*100, 3)), 'centimeters')
                        print()
                        print(dash)
                        true = 3
                        print()

                    else:
                        print(error)
                        print()

            #for type 2 to others
            elif (englishU == '2'):
                while (true == 2 ):
                    print('Convert to which metric units:')
                    print('   For kilometers type:  1')
                    print('   For meters type:      2')
                    print('   For centimeters type: 3')
                    print()
                    targetm = str(input('   Choose target metric units (1, 2 or 3): '))
                    print()

                    #when enter 1
                    if (targetm == '1' and true == 2):
                        feet = float(input('Enter the number of feet to convert to kilometers: '))
                        print()
                        print('RESULT:', feet, 'feet =', '{:.3f}'.format(round(feet*0.3048/1000, 3), 'kilometers'))
                        print()
                        print(dash)
                        true = 3
                        print()
                    #when enter 2
                    elif (targetm == '2' and true == 2):
                        feet = float(input('Enter the number of feet to convert to meters: '))
                        print()
                        print('RESULT:', feet, 'feet =', '{:.3f}'.format(round(feet*0.3048, 3), 'meters'))
                        print()
                        print(dash)
                        true = 3
                        print()

                    #when enter 
                    elif (targetm == '3' and true == 2):
                        feet = float(input('Enter the number of feet to convert to centimeters: '))
                        print()
                        print('RESULT:', feet, 'feet =', '{:.3f}'.format(round(feet*0.3048*100, 3)), 'centimeters')
                        print()
                        print(dash)
                        true = 3
                        print()

                    else:
                        print(error)
                        print()


            #for type 3 to others
            if (englishU == '3'):
                while (true == 2):
                    print('Convert to which metric units:')
                    print('   For kilometers type:  1')
                    print('   For meters type:      2')
                    print('   For centimeters type: 3')
                    print()
                    targetm = str(input('   Choose target metric units (1, 2 or 3): '))
                    print()

                    #when enter 1
                    if (targetm == '1' and true == 2):
                        inches = float(input('Enter the number of inches to convert to kilometers: '))
                        print()
                        print('RESULT:', inches, 'inches =', '{:.3f}'.format(round(inches*0.3048/1000/12, 3)), 'kilometers')
                        print()
                        print(dash)
                        true = 3
                        print()
                        
                    #when enter 2
                    elif (targetm == '2' and true == 2):
                        inches = float(input('Enter the number of inches to convert to meters: '))
                        print()
                        print('RESULT:', inches, 'inches =', '{:.3f}'.format(round(inches*0.3048/12, 3)), 'meters')
                        print()
                        print(dash)
                        true = 3
                        print()

                    #when enter 
                    elif (targetm == '3' and true == 2):
                        inches = float(input('Enter the number of inches to convert to centimeters: '))
                        print()
                        print('RESULT:', inches, 'inches =', '{:.3f}'.format(round(inches*0.3048*100/12, 3)), 'centimeters')
                        print()
                        print(dash)
                        true = 3
                        print()

                    else:
                        print(error)
                        print()

    
    #for answer 2                
    elif (eorm == '2'): 
        while (true == 2):
            print('Select metric units to convert to English equivalent:')
            print('   For kilometers type:  1')
            print('   For meters type:      2')
            print('   For centimeters type: 3')
            print()
            metricU = str(input('Choose metric units to convert (1, 2 or 3): '))
            print()

            if (metricU != '1' and metricU != '2' and metricU != '3'):
                print(error)
                print()
                
            elif (metricU == '1'):
                while (true == 2):
                    print('Convert to which English units:')
                    print('   For miles type:  1')
                    print('   For feet type:   2')
                    print('   For inches type: 3')
                    print()
                    targetE = str(input('   Choose target English units (1, 2 or 3): '))
                    print()

                    #when enter 1
                    if (targetE == '1' and true == 2):
                        km = float(input('Enter the number of kilometers to convert to miles: '))
                        print()
                        print('RESULT:', km, 'kilometers =', '{:.3f}'.format(round(km*1000*3.28084/5280, 3)), 'miles')
                        print()
                        print(dash)
                        true = 3
                        print()
                        
                    #when enter 2
                    elif (targetE == '2'  and true == 2):
                        km = float(input('Enter the number of kilometers to convert to feet: '))
                        print()
                        print('RESULT:', km, 'kilometers =', '{:.3f}'.format(round(km*1000*3.28084, 3)), 'feet'), 
                        print()
                        print(dash)
                        true = 3
                        print()

                    #when enter 3 
                    elif (targetE == '3'  and true == 2):
                        km = float(input('Enter the number of kilometers to convert to inches: '))
                        print()
                        print('RESULT:', km, 'kilometers =', '{:.3f}'.format(round(km*1000*3.28084*12, 3)), 'inches')
                        print()
                        print(dash)
                        true = 3
                        print()

                    else:
                        print(error)
                        print()

            #for type 2 to others
            elif (metricU == '2'):
                while (true == 2 ):
                    print('Convert to which English units:')
                    print('   For miles type:  1')
                    print('   For feet type:   2')
                    print('   For inches type: 3')
                    print()
                    targetE = str(input('   Choose target English units (1, 2 or 3): '))
                    print()

                    #when enter 1
                    if (targetE == '1' and true == 2):
                        meters = float(input('Enter the number of meters to convert to miles: '))
                        print()
                        print('RESULT:', meters, 'meters =', '{:.3f}'.format(round(meters*3.28084/5280, 3)), 'miles')
                        print()
                        print(dash)
                        true = 3
                        print()
                    #when enter 2
                    elif (targetE == '2' and true == 2):
                        meters = float(input('Enter the number of meters to convert to feet: '))
                        print()
                        print('RESULT:', meters, 'meters =', '{:.3f}'.format(round(meters*3.28084, 3)), 'feet')
                        print()
                        print(dash)
                        true = 3
                        print()

                    #when enter 
                    elif (targetE == '3' and true == 2):
                        meters = float(input('Enter the number of meters to convert to inches: '))
                        print()
                        print('RESULT:', meters, 'meters =', '{:.3f}'.format(round(meters*3.28084*12, 3)), 'inches')
                        print()
                        print(dash)
                        true = 3
                        print()

                    else:
                        print(error)
                        print()


            #for type 3 to others
            if (metricU == '3'):
                while (true == 2):
                    print('Convert to which English units:')
                    print('   For miles type:  1')
                    print('   For feet type:   2')
                    print('   For inches type: 3')
                    print()
                    targetE = str(input('   Choose target English units (1, 2 or 3): '))
                    print()

                    #when enter 1
                    if (targetE == '1' and true == 2):
                        centimeters = float(input('Enter the number of centimeters to convert to miles: '))
                        print()
                        print('RESULT:', centimeters, 'centimeters =', '{:.3f}'.format(round(centimeters*3.28084/5280/100, 3)), 'miles')
                        print()
                        print(dash)
                        true = 3
                        print()
                        
                    #when enter 2
                    elif (targetE == '2' and true == 2):
                        centimeters = float(input('Enter the number of centimeters to convert to feet: '))
                        print()
                        print('RESULT:', centimeters, 'centimeters =', '{:.3f}'.format(round(centimeters*3.28084/100, 3)), 'feet')
                        print()
                        print(dash)
                        true = 3
                        print()

                    #when enter 
                    elif (targetE == '3' and true == 2):
                        centimeters = float(input('Enter the number of centimeters to convert to inches: '))
                        print()
                        print('RESULT:', centimeters, 'centimeters =', '{:.3f}'.format(round(centimeters*3.28084*12/100, 3)), 'inches')
                        print()
                        print(dash)
                        true = 3
                        print()

                    else:
                        print(error)
                        print()

    
    
    #for answer 3 
    elif (eorm == '3'):
        print('Thanks for using our converter. Goodbye!')
        break
    
    
    #for first error message
    else:
        print(error)
        print()
    