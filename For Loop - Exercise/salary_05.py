open_tabs = int(input())
salary_entered = int(input())

facebook_penalty = 150
instagram_penalty = 100
reddit_penalty = 50
total_penalty = 0


for x in range(open_tabs):
    web_site_open = input()

    if web_site_open == "Facebook":
        total_penalty += facebook_penalty
    elif web_site_open == "Instagram":
        total_penalty += instagram_penalty
    elif web_site_open == "Reddit":
        total_penalty += reddit_penalty

    if total_penalty >= salary_entered:
        print(f"You have lost your salary.")
        break

else:
    print(f"{salary_entered - total_penalty}")



