friends=["Anu","Vinu","Sonu","Meenu","Neenu"]

#create list of tuples containg name and length of name
friend_length=[]

for name in friends:
    friend_length.append((name,len(name)))

#display
print("Friends list:",friends)
print("List of tuples:",friend_length)
