# Write code for algorithm 4 below
#4. Write a function that calculates the value of 'a' to the power of 'b'.
def power(a, b):
    if b == 0:
        return 1
    else:
        return a*power(a, b-1)

print(power(3, 2))