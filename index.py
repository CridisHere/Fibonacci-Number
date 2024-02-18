#WAP in Python to print the Fibonacci numbers up to nth term.
# The Fibonacci sequence is the series of numbers in which the next term is the sum of the previous two terms.
# For example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# The first two terms of the Fibonacci sequence are 0 followed by 1.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a+b
x=int(input("Enter the number of terms: "))
fibonacci(x)  # prints the x numbers in the Fibonacci sequence