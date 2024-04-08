
lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium_volume = lenght * width * height
aquarium_volume_liters = aquarium_volume * 0.001
percent = percent / 100

liters_needed = aquarium_volume_liters * (1 - percent)
print(liters_needed)