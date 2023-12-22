import math

numbers = []

while True:
    num_input = input("Enter some digits (Provide Blank `" "` to Begin Calculations): ")

    if num_input == "":
        break

    try:
        numbers.append(round(float(num_input), 4))
    except ValueError:
        print("Enter a valid number.")

average = round(sum(numbers) / len(numbers), 4)
std_deviation = round(math.sqrt(sum((x - average) ** 2 for x in numbers) / len(numbers)), 4)

print(f"Average: {average}")
print(f"Standard Deviation: {std_deviation}")
