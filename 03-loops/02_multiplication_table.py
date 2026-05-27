# You are developing a feature in an educational app that displays multiplication tables.

# Tasks:


# Using a for loop and range(), generate the multiplication table for number from 1 to 10.
# Return a list of strings in the following format:
# "number x i = result"
# (Example: "3 x 4 = 12")

num = int(input("Enter the number to get its multiplication number : "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")