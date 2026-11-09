#Exercise5
#type("12") results in <class 'str'>, type(12) results in <class 'int'>, type(12.0) results in <class 'float'>, type(True) results in <class 'bool'>, "5" + "3" results in "53", 5 + 3 results in 8
# it treated the quotations as strings and non quotations as numbers 

#self assessmnet questions 
# question 1: The error said it can't multuply sequence by non int of type 'float', it can't multiply a string by a number
#question 2: it sees 5 and 3 as a string and not numbers so it won't add they but rather combine them. to be able to use them as number they need to be converted
#question 3: I would use variables, types, and f-strings to calculate revenue and profit as a potential entrepruner and use the f-strings to display the results. The conversions will help during calcuations and to create reports. 

#Exercise1
product="notebook"
print(type(product))
unit_price= 4.99
print(type(unit_price))
quantity=12
print(type(quantity))
in_stock=True
print(type(in_stock))

#Exercise2
print(f"{quantity} units of Notebook at ${unit_price} each = ${unit_price * quantity:.2f}")

#Exercise3
product=input("Enter product: ")
unit_price=float(input("Enter price: "))
quantity=int(input("Enter quantity: "))

print(f"{quantity} units of {product} at ${unit_price} each = ${unit_price * quantity:.2f}")

#Exercise4
product=input("Enter product: ")
unit_price=float(input("Enter price: "))
quantity=int(input("Enter quantity: "))
unit_cost=float(input("Enter unit cost: "))

revenue=unit_price * quantity
margin=((unit_price - unit_cost) / unit_price) * 100

print(f"Product: {product}")
print(f"Price: ${unit_price}")
print(f"Qty: {quantity}")
print(f"Revenue: ${revenue}")
print(f"Margin: {margin}%")


