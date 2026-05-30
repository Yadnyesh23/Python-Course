# ou are building an Order Invoice Generator system for a restaurant. The function should be versatile enough to accept a customer's name, a flexible number of ordered items, and a set of dynamic extra charges (like tax, service charge, etc.).

# Your Tasks:
# Function: generate_invoice(customer_name: str, *items: str, **charges: float) -> str

# customer_name: optional; defaults to "Guest" if not provided.

# items: an arbitrary number of strings representing food items ordered.

# *charges: keyword arguments representing different charges like tax=50.0, service=20.0, delivery=15.0, etc.

# Invoice Structure:

# Header: Invoice for <customer_name>
# Items Section (only if items are provided):
# Line: Items:
# Each item on its own line with format: - <item_name>
# Charges Section (only if charges are provided):

# Line: Charges:

# Each charge on its own line with format: <Charge_name>: <amount>

# At the end, the display Total Amount Due: ₹<total>.

# Important Notes:

# Sum only the values from *charges for total.

# Items are only for listing, not costing.

# Charge names should be capitalized (e.g., tax becomes Tax)

# Use \n to join all lines into a single string

def generate_invoice(customer_name="Guest", *items , **charges):
    lines = []
    
    lines.append(f"Invoice for {customer_name}")
    
    if items:
        lines.append("Items :")
        for item in items:
            lines.append(f"- {item}")
    
    if charges:
        lines.append("Charges :")
        for key, value in charges.items():
            lines.append(f"{key.capitalize()}: {value}")
            
    total = sum(charges.values())
    lines.append(f"Total Amount Due: ₹{total}")
    
    return "\n".join(lines)


invoice = generate_invoice('Yadnyesh', 'Pizza', 'Burger', tax=50, service=20)

print(invoice)