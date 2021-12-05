FILE_NAME = "input.txt"

horizontal_position = 0
depth = 0

with open(FILE_NAME, "r") as f:
    for line in f:
        movement, value = line.split(" ")
        if movement == "forward":
            horizontal_position += int(value)
        elif movement == "up":
            depth -= int(value)
        elif movement == "down":
            depth += int(value)
        else:
            raise ValueError(f"Movement \"{movement}\" unrecognized")
    
print(f"Final position : horizontal position = {horizontal_position} and depth = {depth}")
print(f"So the answer is {horizontal_position * depth}")