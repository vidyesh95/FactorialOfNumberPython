# Python program to find factorial of given number using recursive method.

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = input("Enter the number : ")
print("Factorial of", number, "is", factorial(int(number)))
