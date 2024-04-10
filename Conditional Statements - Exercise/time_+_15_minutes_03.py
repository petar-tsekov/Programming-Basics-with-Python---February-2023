#Input

hours = int(input())
minutes = int(input())

#Logic

total_hours = hours * 60
total_minutes = minutes + total_hours + 15


hours = total_minutes // 60
minutes = total_minutes % 60

#Otput

if hours > 23:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")

else:
    print(f"{hours}:{minutes}")
