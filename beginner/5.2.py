total_jumping_jacks=100
completed=0

for i in range(10):#10 sets of 10 jumping jacks
    completed+=10
    print("You completeed",completed,"jumping jacks.")

    if completed==100:
        print("Congratulations!you completeed the workout.")
        break
    tired=input("Are you tired?(yes/y or no/n)").lower()
    if tired=="yes" or tired=="y":
        skip=input("Do you want to skip the remaining sets?(yes/y or no/n)").lower()
        if  skip=="yes" or skip=="y":
            print("you completed a total of",completed,"jumping jacks")
            break
        else:
            print(total_jumping_jacks-completed,"jumping jacks remaining")
    else:
        print(total_jumping_jacks-completed,"jumping jacks remaining")
    
