# description = "Aromatic and Bold"
# print(f"Reverse description : {description[::-1]}")
label_text = "Chai spécial"
encoded_text = label_text.encode("utf-8")
decoded_text = encoded_text.decode("utf-8")
print(f"Non encoded label : {label_text}")
print(f"Encoded label : {encoded_text}")
print(f"Decoded label : {decoded_text}")