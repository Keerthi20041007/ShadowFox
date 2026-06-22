#function to format a number using the given format specifier
def format_number(num,fmt):
    return format(num,fmt)

number=int(input("enter a number:"))
specifier=input("enter the format specifier:")

#calling the function
result=format_number(number,specifier)

#displaying the result
print("Formatted result=",result)

#identifying the representation
if specifier=='o':
    print("Representation used:octacl(Base 8)")
