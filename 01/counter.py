
FILE_NAME = "input.txt"

def main():
    increase_count = 0
    prev_num = 20_000_000
    with open(FILE_NAME, "r") as f:
        for line in f:
            num = int(line)
            if num > prev_num:
                increase_count += 1
            prev_num = num
    print(f"Number of increases : {increase_count}")

if __name__ == "__main__":
    main()