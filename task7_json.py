import json

# Open and read the JSON file
with open('products.json', 'r') as file:
    products = json.load(file)  # Parse JSON data

# Display header
print("{:<15} {:<10} {:<10}".format("Name", "Price", "Quantity"))
print("-" * 35)

# Display each product in a table row
for product in products:
    print("{:<15} {:<10} {:<10}".format(
        product['name'], product['price'], product['quantity']
    ))
