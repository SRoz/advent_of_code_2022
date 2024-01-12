with open("inputs/day3.txt") as fn:
    input = fn.read()


with open("inputs/day3_test.txt") as fn:
    test_input = fn.read()

    
total = 0 
for line in input.splitlines():
    first, second = line[:len(line)//2], line[len(line)//2:]
    shared = set(first).intersection(set(second))

    shared = list(shared)[0]
    val = ord(shared) - 96 if shared.islower() else ord(shared)-38

    total += val

print(total)


total = 0
lines = input.splitlines()
for i in range(len(lines)//3):
    shared = set(lines[i*3]).intersection(lines[i*3+1]).intersection(lines[i*3+2])
    shared = list(shared)[0]
    val = ord(shared) - 96 if shared.islower() else ord(shared)-38

    total += val

print(total)