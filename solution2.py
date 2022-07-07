# Write code for algorithm 2 below
#2. Write a function that prints the natural numbers from 1 to n.
def natural_numbers(x, y):
    if x > y:
        return
    else:
        print(x)
        natural_numbers(x + 1, y)

n=5
natural_numbers(1, n)