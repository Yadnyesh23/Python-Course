# You're building a Function Behavior Analyzer to showcase different types of Python functions in action. Implement the following:



# Pure Function

# Write a function pure_add(a, b) that takes two integers and returns their sum.

# It should not rely on or modify any external state.



# Impure Function

# Define a global variable counter.

# Implement impure_increment() that increases the counter and returns its value.



# Recursive Function

# Implement factorial_recursive(n) that returns the factorial of a given number using recursion.

# Handle base case correctly (e.g., factorial_recursive(0) = 1).



# Lambda Function with map()

# Write a function square_list(nums) that uses a lambda inside map() to return a new list with the squares of the numbers in the input list.

# Pure FUnction 

def pure_add(a,b):
    sum = a + b
    return sum

a = int(input("Enter a number a :"))
b = int(input("Enter a number b:"))

sum = pure_add(a,b)
print(f'Sum : {sum}')

# Unpure function

counter=0

def impure_increment():
    global counter
    counter += 1
    return counter

count = impure_increment()
print(count)

# Recursivve function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

value = factorial_recursive(3)
print(value)

# Lambda Function 
numbers = [1,2,3,4,5,6,7,8,9,10]
squared     = list(map(lambda x: x**2, numbers)) 
print(squared)