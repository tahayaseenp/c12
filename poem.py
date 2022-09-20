# Write a function in python to count the number of lines in "POEM.txt" that begins using upper case
# Write a function in python to read lines from the file "POEM.txt" and count how many how many times the word "corona" exists in file
# Write a function dispS() in python to read the text file "POEM.txt" and display those lines that start with "S"
# Write a function COUNTSIZE() in Python to read the file "POEM.txt" and display size of the file
# Write a function ATOEDISP() for each requirement in Python to read the file "NEWS.txt" and
#   Display "E" in place of all the occurence of "A" in the word COMPUTER
#   Display "E" in place of all the occurence of "A"
#       I SELL COMPUTARS. I HAVE A COMPUTAR. I NEED A COMPUTAR. I WANT A COMPUTAR. I USE THAT COMPUTAR. MY COMPUTAR CRASHED.

import sys


def lines():
    c = 0
    for i in open("poem.txt").readlines():
        if i[0].isupper() == True:
            c += 1
    return "Lines starting from capital letters :", c


def word():
    return "Number of times the word corona appears :", open("poem.txt").read().lower().count("corona")


def dispS():
    for i in open("poem.txt").readlines():
        if i[0] == 'S':
            print(i)


def COUNTSIZE():
    return "Size of file is", len(open("poem.txt").read())


def ATOEDISP1():
    return open("news.txt").read().replace("COMPUTARS", "COMPUTERS")


def ATOEDISP2():
    return open("news.txt").read().replace("A", "E")

while True:
    print("""
    1. Count the number of lines in "POEM.txt" that begins using upper case
    2. Read lines from the file "POEM.txt" and count how many how many times the word "corona" exists in file
    3. Read the text file "POEM.txt" and display those lines that start with "S"
    4. Read the file "POEM.txt" and display size of the file
    5. Read the file "NEWS.txt" and display "E" in place of all the occurence of "A" in the word COMPUTER
    6. Read the file "NEWS.txt" and display "E" in place of all the occurence of "A"
    0. Exit
    """)

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print(lines())

    elif ch == 2:
        print(word())

    elif ch == 3:
        dispS()

    elif ch == 4:
        print(COUNTSIZE())

    elif ch == 5:
        print(ATOEDISP1())

    elif ch == 6:
        print(ATOEDISP2())

    elif ch == 0:
        sys.exit("Thank You!")