# Write a program to accept the input of employees from the user and store it in a CSV file and retrieve it to display to the user
import csv
import sys


def em_in():
    while True:
        emno = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        salr = float(input("Enter employee salary: "))
        dept = input("Enter employee department: ")
        w.writerow([emno, name, salr, dept])
        c = input("Would you like to continue? (y/n)")
        if c.lower() != 'y':
            break

file = open("employee.csv", "w")
w = csv.writer(file)
w.writerow(["Employee ID", "Employee Name", "Employee Salary", "Employee Department"])
file.close()
file = open("employee.csv", "a")
w = csv.writer(file)
em_in()
file.close()
sys.exit("Thank You!")