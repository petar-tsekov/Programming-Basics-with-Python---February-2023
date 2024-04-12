
petar_budget = float(input())
gpu_qty = int(input())
cpu_qty = int(input())
ram_memory_qty = int(input())

gpu_price = gpu_qty * 250
cpu_price_qty = gpu_price * 0.35
total_cpu_qty = cpu_price_qty * cpu_qty
ram_memory_price_qty = gpu_price * 0.10
total_ram_memory_price_qty = ram_memory_qty * ram_memory_price_qty

total_price = gpu_price + total_cpu_qty + total_ram_memory_price_qty

if gpu_qty > cpu_qty:
    total_price -= total_price * 0.15

if petar_budget >= total_price:
    remained_budget = petar_budget - total_price
    print(f"You have {remained_budget:.2f} leva left!")
elif total_price > petar_budget:
    needed_budget = total_price - petar_budget
    print(f"Not enough money! You need {needed_budget:.2f} leva more!")