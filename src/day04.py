with open("inputs/day4.txt", 'r') as fn:
    input = fn.read()
 
def count_contained_ranges(input, part=1):
    pairs = input.strip().split("\n")
    contained_count = 0
    for pair in pairs:
        range1, range2 = pair.split(",")
        start1, end1 = map(int, range1.split("-"))
        start2, end2 = map(int, range2.split("-"))
        if part==1:
            if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
                contained_count += 1
        if part==2:
            if (start1 <= start2 and end1 >= start2) or (start2 <= start1 and end2 >= start1):
                contained_count += 1

    return contained_count

print(count_contained_ranges(input, part=1))
print(count_contained_ranges(input, part=2))
