# File: Payroll.py
# Student: Ting Wei Wu
# UT EID: tw28634
# Course: CS303E
# 
# Date: February 08, 2022
# Description of Program: This is program is designed for computing the Net paid after deductions.

# Input
name = str(input("Enter employee's name: "))
h = float(input("Enter number of hours worked in a week: "))
r = float(input("Enter hourly pay rate: "))
ftwr = float(input("Enter federal tax withholding rate: "))
stwr = float(input("Enter state tax withholding rate: "))

# Some Variables
gp = h*r

# Output
print("")
print("Employee Name:", name)
print("Hours Worked: " + str(format (h, "0.1f")))
print("Pay Rate: $" + str(format (r, "0.2f")))
print("Gross Pay: $" + str(format (gp, "0.2f")))
print("Deductions: ")
# Deductions
print("  Federal Withholding (" + str(format(ftwr*100, "0.1f")) + "%): $" + format(gp*ftwr, "0.2f"))
print("  State Withholding (" + str(format(stwr*100, "0.1f")) + "%): $" + format(gp*stwr, "0.2f"))
print("  Total Deduction: $" + (format(gp*ftwr + gp*stwr, "0.2f")))
print("Net Pay: $" + (format(gp - (gp*ftwr + gp*stwr), "0.2f")))