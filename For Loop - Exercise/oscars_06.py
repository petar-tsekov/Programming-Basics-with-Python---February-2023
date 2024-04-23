actor_name = input()
academy_point = float(input())
jury_qty = int(input())


points_needed = 1250.50


for x in range(jury_qty):
    jury_name = input()
    point_of_jury = float(input())

    academy_point = academy_point +((len(jury_name) * point_of_jury) / 2)

    if academy_point > points_needed:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_point:.1f}!")
        break

else:
    print(f"Sorry, {actor_name} you need {points_needed-academy_point:.1f} more!")





