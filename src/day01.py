
with open("inputs/day1.txt") as fn:
    input = fn.read()

elf_cal_sums = [sum([int(j) for j in i.split("\n")]) for i in input.split("\n\n")]

print(max(elf_cal_sums))
print(sum(sorted(elf_cal_sums)[-3:]))


