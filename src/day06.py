def solve(datastream, n):
    i=0
    for i, c in enumerate(zip(*[datastream[i:] for i in range(n)])):
        if len(set(c)) == n:
            break
    print(i+n)

with open("inputs/day6.txt") as fn:
    input = fn.read()

solve(input, n=4)
solve(input, n=14)
