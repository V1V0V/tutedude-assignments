x = int(input("Enter a Number:"))
def factorial(x):
    if x<=1:
        return 1
    else:
        return x * factorial(x-1)
        
print(f"The Factorial of {x} is: {factorial(x)}")
    