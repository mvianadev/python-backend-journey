# F-strings - forma moderna de formatear

name: str = "Ana"
age: int = 28
salary: float = 45000.75

# F-strings básicos
print(f"Hello, my name is {name}")
print(f"I am {age} years old")
print(f"My salary is ${salary}")

# F-strings con formato
print(f"Salary formatted: ${salary:,.2f}")  # 45,000.75
print(f"Next year I will be {age + 1} years old")

# Calculadora simple con f-strings
price: float = 99.99
quantity: int = 3
total = price * quantity

print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")