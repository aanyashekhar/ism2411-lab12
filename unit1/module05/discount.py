#starter code from lab 5
total=float(input("enter cart total: $"))

#add your if/elif/else here 
#exercise 1
if total>=500:
    discount=0.15
elif total>=200:
    discount=0.1
elif total>=100:
    discount=0.05
else:
    discount=0

#discount = 0 #replace with correct logic 
final=total*(1-discount)
print(f"discount:{discount*100:.0f}%")

#exercise 2
if final> 1000: #strictly greater than
    status="manager_approval_required"
else:
    status="auto_approved"

print(status)

#exercise 3
region="South"

if region=="South" and total>=100:
    extra_discount=0.02 
    print("Region bonus applied: additional 2% off")
else:
    extra_discount=0

final=total*(1-(discount+extra_discount))
print(final)

#exercise 4
customer_type="wholesale"
if region=="South" and total>100 and customer_type=="wholesale":
    extra_discount=0.03

#excercise 5
amount=0

if amount<=0:
    print("SUSPICIOUS")
elif amount>10000:
    print("NORMAL")
else:
    print("LARGE--REVIEW REQUIRED")

#excercise 6
total_spent_this_year=2500
orders_this_year=6
has_outstanding_balance=False 

vip_upgrade=True
if total_spent_this_year>2000 or orders_this_year>10:
    vip_upgrade=True
else:
    vip_upgrade=False

