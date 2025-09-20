"""

Function: A set of code defined for a particular/specific task is considered as a function where a function can take input => Processes it => It can show output.

Rules of using function:
1. Define: Define the function and wait for calling.
2. Call: mention the function name and give the input value. Remember without calling, a function never get excecuted. A function without being called means a useless machine.

"""

def even_odd(number):
    if number % 2 == 0 :
        return f"The {number} is even"
    else :
        return f"The {number} is odd"
n = int(input("Inter any number: "))
result = even_odd(n)
print(result)