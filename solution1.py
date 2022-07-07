# Write code for algorithm 1 below
#1. Write a program that takes a positive number as an argument and prints the numbers from n to zero.
def minus(n):
    if n == 0:
        return
    else:
        print(n)
        minus(n-1)

n = 10
minus(n)