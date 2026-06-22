height=float(input("Ener height in meters:"))
weight=float(input("enter weight in kilgram:"))

bmi=weight/(height**2)

#determine BMI catprintegory
if bmi>=30:
    print("Obesity")
elif bmi>=25:
    print("Overweight")
elif bmi>18.5:
    print("Normal")
else:
    print("Underweight")
    
    
