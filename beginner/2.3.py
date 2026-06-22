distance=int(input("Enter the distance in meter:"))
time_minutes=int(input("enter the time in minutes:"))
time_seconds=time_minutes*60
speed=distance/time_seconds
print("the time in seconds:",time_seconds)
print("speed=",int(speed),"m/s")
