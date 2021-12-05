FILE_NAME = "input.txt"
NUMBER_OF_BITS = 12

def readlines(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line

# We will count the presence of each bit in each row and store it in a list
count_one_per_bit = [0] * NUMBER_OF_BITS
num_lines = 0
for line in readlines(FILE_NAME):
    num_lines += 1
    for i, char in enumerate(line):
        if char == "1":
            count_one_per_bit[i] += 1
print(count_one_per_bit, num_lines)

# Find the values
mid_num_lines = num_lines // 2
gamma_str, epsilon_str = "", ""
for count in count_one_per_bit:
    if count < mid_num_lines: # "1" is the least common bit
        gamma_str += "0"
        epsilon_str += "1"
    else: # "1" is the most common
        gamma_str += "1"
        epsilon_str += "0"

gamma_rate, epsilon_rate = int(gamma_str, 2), int(epsilon_str, 2)
print(f"Gamma rate = {gamma_rate}, Epsion rate = {epsilon_rate}")
print(f"So the answer is {gamma_rate * epsilon_rate}")