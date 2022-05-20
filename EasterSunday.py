# File: EasterSunday.py
# Student: Ting Wei Wu
# UT EID: tw28634
# Course: CS303E
# 
# Date: February 03, 2022
# Description of Program: This is program is designed for computeing the date of Easter Sunday for a specified year.

y = int(input("Enter year: ")) #user input
a = y % 19 
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4 
k = c % 4
m = (a + 11 * h) // 319
r =  (2 * e + 2 * j - k - h + m + 32) % 7 
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

print("In", y, "Easter Sunday is on month", n, "and day", p)



