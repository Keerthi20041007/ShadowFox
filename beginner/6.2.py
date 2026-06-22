your_expense={}

partner_expense={}
categories=["Hotel","Food","Transportation","Attractions","Miscellaneous"]
print("Enter your expense")
for category in categories:
    your_expense[category]=float(input(f"{category}:"))

print("\nEnter your  partner's expense")
for category in categories:
    partner_expense[category]=float(input(f"{category}:"))

your_total=sum(your_expense.values())
partner_total=sum(partner_expense.values())
print("your total expense=",your_total)
print("partner's total expense=",partner_total)

#determine who spent more
if your_total>partner_total:
    print("You spent more than your partner")
elif partner_total>your_total:
    print("Partner spent more than you")
else:
    print("Both spent the same amount")

#find the category with maximum difference

max_dif=0
category_name=""

for category in your_expense:
    difference=abs(your_expense[category]-partner_expense[category])

    if difference>max_dif:
        max_dif=difference
        category_name=category

print("\nExpense category with maximum difference=",category_name)
print("\nDifference in spending=",max_dif)
