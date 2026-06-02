class ChaiOrder:

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, orderdata):
        return cls(
            orderdata["tea_type"],
            orderdata["sweetness"],
            orderdata["size"],
        )

    @classmethod
    def from_string(cls, orderstring):
        tea_type, sweetness, size = orderstring.split("-")
        return cls(tea_type, sweetness, size)


# Creating object from dictionary
order_data = {
    "tea_type": "Masala Chai",
    "sweetness": "Medium",
    "size": "Large"
}

order1 = ChaiOrder.from_dict(order_data)

print(order1.tea_type)
print(order1.sweetness)
print(order1.size)


# Creating object from string
order2 = ChaiOrder.from_string("Ginger Chai-Low-Small")

print(order2.tea_type)
print(order2.sweetness)
print(order2.size)