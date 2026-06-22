#initial justice leauge list
justice_league=["Superman","Batman","Wonder woman","Flash","Aquaman","Green Lantern"]

#calculate the number of members
print("1.Number of members:",len(justice_league))
print(justice_league)

#Add  batgirl and nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2.After  adding Batgirland Nightwing:")
print(justice_league)

#move the wonder women to the beginning
justice_league.remove("Wonder woman")
justice_league.insert(0,"Wonder woman")
print("\n3.After making Wonder woman the leader:")
print(justice_league)

#Move superman between Aquaman and flash
justice_league.remove("Superman")
aquaman_index=justice_league.index("Aquaman")
justice_league.insert(aquaman_index+1,"Superma")
print("\n4.After separating Aquaman and Flas:")
print(justice_league)

#Replace the team with new member
justice_league=["Cyberg","shazam","Hawkgirl","Martain manhunter","Green Arrow"]
print("\n.New justice league team:")
print(justice_league)

#sort alphabetically
justice_league.sort()
print("\n6.Sorted justice league:")
print(justice_league)

#new leader
print("\nNew leader:",justice_league[0])
