
#self assesment question 
#question 1: an accumulator pattern is a loop that retains a total value of a variable as it goes through values. the three steps are initialize a variable before the loop, update the variable inside the loop using each item, and print final result after loop. If a step is missing a the loop 
#question 2: while loop is longer than for loop beccause it needs more lines of code. for loop is easier to read but while loop is more flexible 
#question 3: can use loop on dataset with monthly sales data to calculate total sales and count the transactions. 

#excercise 1
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

#excercise 2
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1
average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

#excercise 3
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest sale: ${current_max}")

#excercise 4
over_100_count = 0
over_100_total = 0
for sale in sales:
    if sale > 100:
        over_100_count += 1
        over_100_total += sale
print(f"Sales over $100: {over_100_count}")
print(f"Total of those sales: ${over_100_total}")

#excercise 5
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found — ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

#excercise 6
total = 0
i = 0
while i < len(sales):
    total += sales[i]
    i += 1
print(f"Total: ${total}")

#excercise 7
for sale in sales:
    if sale >= 200:
        discount_rate = 0.10
    elif sale >= 100:
        discount_rate = 0.05
    else:
        discount_rate = 0
    discounted_price = sale * (1 - discount_rate)
    print(f"${sale} → {discount_rate:.0%} discount → ${discounted_price:.2f}")