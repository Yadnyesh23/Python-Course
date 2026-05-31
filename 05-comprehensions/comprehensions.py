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

# Set Comprehensions

favourite_teas = [
    "Masala Tea", "Green Tea", "Masala Tea",
    "Lemon Tea", "Green Tea", "Elaichi Tea"
]

unique_chais = {chai for chai in favourite_teas}
print(unique_chais)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)

# Dictionary Comprehensions

chai_price_inr = {
    "Masala Chai" : 40,
    "Green tea" : 60,
    "Lemon tea" : 200
}

chai_price_usd = {tea : price/80  for tea, price in chai_price_inr.items()}
print(f"Price in Inr : {chai_price_inr}")
print(f"Price in Inr : {chai_price_usd}")