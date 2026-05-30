# List Comprehensions

menu = [
    "Masala Chai",
    'Iced Lemon Tea',
    "Green Tea",
    'Iced Peach Tea',
    'Ginger tea'
]

iced_tea = [tea for tea in menu if 'Iced' in tea]

print(iced_tea)

nums = [1,2,3,4,5]
squares = [x**2 for x in nums ]
print(squares)