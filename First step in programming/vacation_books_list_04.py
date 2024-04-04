pages_count = int(input())
pages = int(input())
days_count = int(input())

total_reading_time = pages_count // pages
reading_hours_needed = total_reading_time / days_count

print(reading_hours_needed)