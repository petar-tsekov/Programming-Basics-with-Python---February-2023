
steps_goal = 10000

total_steps = 0

steps_int = 0

while True:
    steps_entered = input()

    if steps_entered != "Going home":
        steps_int = int(steps_entered)
        total_steps = total_steps + steps_int

        if total_steps >= steps_goal:
            break
    elif steps_entered == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        break

if total_steps >= steps_goal:
    print(f"Goal reached! Good job!")
    print(f"{total_steps - steps_goal} steps over the goal!")
else:
    print(f"{steps_goal - total_steps} more steps to reach goal.")
