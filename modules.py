import random

numbers = []
for i in range(1, 91):
    numbers.append(i)


def create_sheet():
    sheet = list(random.sample(numbers, 15))
    return sorted(sheet)


if __name__ == "__main__":
    print("This is modules.py")
