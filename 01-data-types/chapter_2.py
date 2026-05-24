# # Write a Python program that performs the following operations and prints the results
# # Addition , Subtraction , Multiplication , Division (float result), Floor Division (integer result), Modulus (remainder)

a = 10
b = 5
sum  = a + b
diff  = a - b
Multiplication  = a * b
accurate_division = a / 3
approx_division = a//3
remainder = a % b
exponentian = a ** b

print(f"Sum  of 10 and 5 is {sum}")
print(f"Differebce of 10 and 5 is {diff}")
print(f"Multiplication of 10 and 5 is {Multiplication}")
print(f"Accurate division of 10 and 5 is {accurate_division}")
print(f"Approx Division of 10 and 3 is {approx_division}")
print(f"Remainder of 10 and 3 is {remainder}")
print(f"Exponential of 10 to power 5 is {exponentian}")


initial_temp = 95.5
final_temp = 95.49999999999999

print(f"Initial temp : {initial_temp}")
print(f"Final temp : {final_temp}")
print(f"Difference : {initial_temp - final_temp}")

# You’re deciding whether to go for a walk based on two real-life conditions:

# is_sunny = True
# have_umbrella = False

# Print the result of the following:

# Is it not sunny today?

# Do you not have an umbrella?

# Should you go for a walk if it’s sunny and you don’t need an umbrella?

# Should you go for a walk if it’s sunny or if you have an umbrella?

is_sunny = True
have_umbrella = False

print(f"Is it not sunny today ? : {not is_sunny}")
print(f"Do you not have an umbrella? :  {not have_umbrella}")
print(f"Should you go for a walk (If its sunny and dont need umbrella)  : {is_sunny and not have_umbrella}")
print(f"Should you go for a walk (If its sunny or have umbrella)  : {is_sunny or  have_umbrella}")