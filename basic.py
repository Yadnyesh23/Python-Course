# string = input("Enter a string t check whether it is palindrome or not : ")
# reversedString = string[::-1]

# if(string == reversedString):
#     print(f"{string} is palindrome.")
# else :
#     print(f"{string} is not palindrome.")

# for i in range(1, 11):
#     print(f"Servving chai to token #{i}")

# Method 1
divisible_by_4 = {num for num in range(1,22) if num % 4 == 0}
print(divisible_by_4)

# Method 2
divisible_by_4 = set()

for num in range(1,22):
    if num % 4 == 0:
        divisible_by_4.add(num)
        
print(divisible_by_4)