country = input()
discipline = input()

total_points = 20
current_points = 0
if country == "Russia":
    if discipline == "ribbon":
        current_points = 9.100 + 9.400
    elif discipline == "hoop":
        current_points = 9.300 + 9.800
    elif discipline == "rope":
        current_points = 9.600 + 9.000
elif country == "Bulgaria":
    if discipline == "ribbon":
        current_points = 9.600 + 9.400
    elif discipline == "hoop":
        current_points = 9.550 + 9.750
    elif discipline == "rope":
        current_points = 9.500 + 9.400
elif country == "Italy":
    if discipline == "ribbon":
        current_points = 9.200 + 9.500
    elif discipline == "hoop":
        current_points = 9.450 + 9.350
    elif discipline == "rope":
        current_points = 9.700 + 9.150

diffrence = total_points - current_points
diffrence = (diffrence/total_points)*100
print(f"The team of {country} get {current_points:.3f} on {discipline}.")
print(f"{diffrence:.2f}%")

