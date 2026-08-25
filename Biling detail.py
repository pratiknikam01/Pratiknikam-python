print("======Billing details======")

rice_qty=float(input("Enter the qty of rice:"))
rice_price_per_kg=50
rice_total=rice_qty*rice_price_per_kg

sugar_qty=float(input("Enter the qty of sugar:"))
sugar_price_per_kg=100
sugar_total=sugar_qty*sugar_price_per_kg

oil_qty=float(input("Enter the qty of oil:"))
oil_price_per_kg=150
oil_total=oil_qty*oil_price_per_kg

print("======Total amount======")

print("rice",rice_total)
print("sugar",sugar_total)
print("oil",oil_total)

Total_bill=rice_total+sugar_total+oil_total

print("Total bill",Total_bill)
Discount=0
if Total_bill>=1000:
    Discount=Total_bill*0.1
    print("Discount",Discount)
elif Total_bill>=500:
    Discount=Total_bill*0.5
    print("Discount",Discount)
else:
    print("No Discount",Discount)
    
Final_bill=Total_bill-Discount
print("Final_Bill",Total_bill)