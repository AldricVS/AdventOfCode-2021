FILE_NAME = "input.txt"

horizontal_position = 0
depth = 0
aim = 0

with open(FILE_NAME, "r") as f:
    for line in f:
        movement, value = line.split(" ")
        if movement == "forward":
            horizontal_position += int(value)
            depth += aim * int(value)
        elif movement == "up":
            aim -= int(value)
        elif movement == "down":
            aim += int(value)
        else:
            raise ValueError(f"Movement \"{movement}\" unrecognized")
    
print(f"Final position : horizontal position = {horizontal_position} and depth = {depth}")
print(f"So the answer is {horizontal_position * depth}")