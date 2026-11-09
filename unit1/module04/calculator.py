#revenue, margins and discount calculator 


#3 self assesment questions 
#question 1: it would not calculate it as 10 percent but rather a crazy large number. Python wouldn't crash it owuld just produce a wrong answer 
#question 2: for restaurant catering knowing full boxes and loose items of food is helpful
#question 3: I'm least confident about formatting and making small errors in code. I think practice will help 


#exercise 1

price=50
quantity=12
revenue=price*quantity

print(f"Revenue: ${revenue:,.2f}")

#exercise 2

cost=32
price=50
margin=(price-cost)/price
print(f"Margin:{margin:.1%}")

#exercise3
#product a wins if margin_a>margin_b
#product a margin 60#, product b margin (80-60)/80=25%
margin_a=0.60
margin_b=0.25
product_a_wins=margin_a>margin_b
print(f"Product A wins: {product_a_wins}")

#exercise 4
is_premium=price>100 and margin>0.3
#print(f"Is premium: {is_premium}")

price=150
margin=.35

#exercise 5
print(17/5) 
print(17//5)
print(17%5)

#exercise 6

#inputs name, retail_price, cost, quantity_sold, discount_pct

product=input("Enter product name:")
retail_price=float(input("Enter retail price:"))
quantity_sold=int(input("Enter quantity sold:"))
discount_pct=int(input("Enter discount percentage:"))
cost=float(input("Enter cost:"))
print('='*50)
revenue=retail_price*quantity_sold
discounted_revenue=revenue*(1-discount_pct/100)
gross_margin=(retail_price-cost)/retail_price
net_profit=discounted_revenue-(cost*quantity_sold)

#output

print(f"Product: {product}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Discounted revenue: ${discounted_revenue:,.2f}")
print(f"Gross margin: {gross_margin:.1%}")
print(f"Net profit: ${net_profit:,.2f}")



#exercise 7
BOX_SIZE=24 #all uppercase means constant 
items_ordered=int(input("Number of items ordered:")) 
full_boxes=items_ordered//BOX_SIZE
loose_items=items_ordered%BOX_SIZE
exact_fit=loose_items==0
print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")

#stretch a

#retail_price=50
#cost=32
#fixed_costs=1000.0

#contribution=retail_price-cost
#whole_units=int(fixed_costs//contribution)

#print(f"Whole units: {whole_units}")
