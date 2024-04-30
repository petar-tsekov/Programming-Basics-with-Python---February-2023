
length_space = int(input())
width_space = int(input())
height_space = int(input())

total_space = length_space * width_space * height_space
total_boxes = 0

while True:
    boxes_qty = input()
    if boxes_qty == "Done":
        break
    else:
        boxes_qty_int = int(boxes_qty)
    total_boxes = total_boxes + boxes_qty_int

    if total_space < total_boxes:
        break

if total_space < total_boxes:
    print(f"No more free space! You need {total_boxes - total_space} Cubic meters more.")
else:
    print(f"{total_space - total_boxes} Cubic meters left.")


"""length_space = int(input())
width_space = int(input())
height_space = int(input())

total_space = length_space * width_space * height_space
total_boxes = 0

boxes_qty = input()

while boxes_qty != "Done":

    boxes_qty_int = int(boxes_qty)
    total_boxes = total_boxes + boxes_qty_int

    if total_space < total_boxes:
        print(f"No more free space! You need {abs(total_space - total_boxes)} Cubic meters more.")
        break
    boxes_qty = input()

else:
    print(f"{total_space - total_boxes} Cubic meters left.")

"""