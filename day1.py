sum = 0

with open("day1.txt") as f:
    lines = f.readlines()
    for line in lines:
        for char in line[::-1]:
            if char.isdigit():
                sum += int(char)
                break
        for char in line:
            if char.isdigit():
                sum += int(char)*10
                break

print(f"The sum of all calibration values is {sum}")