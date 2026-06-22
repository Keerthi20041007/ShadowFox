import random
count_6=0
count_1=0
two_6s_row=0
previous_roll=0

for i in range(20):#roll the die 20 times
    roll=random.randint(1,6)
    print("Roll",i+1,":",roll)

    if roll==6:
        count_6+=1

    if roll==1:
        count_1+=1
    if roll==6 and previous_roll==6:
        two_6s_row+=1

    previous_roll=roll

print("\nStatistics:")
print("\nNumber of times 6 was rolled:",count_6)
print("\nNumber of imes 1 was rolled:",count_1)
print("\nNumber of times two 6s occurresd in a row:",two_6s_row)


