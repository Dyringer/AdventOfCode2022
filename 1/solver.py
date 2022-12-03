with open("1/input.dat", "r") as fp:
    elves = []
    calories = 0
    for line in fp.readlines():
        if line == "\n":
            elves.append(calories)
            calories = 0
        else:
            calories += int(line.strip())
    print("Max:", max(elves))
    print("Sum of max 3:", sum(sorted(elves)[-3:]))