
with open("inputs/day2.txt") as fn:
    input = fn.read()

game_dict = {
    'A':1,
    'B':2,
    'C':3,
    'X':1,
    'Y':2,
    'Z':3
}


def game(opponent, me):
    score = game_dict[me] - game_dict[opponent]
    return 3*((score + 1) %3) + game_dict[me]

def game2(opponent, me):
    return (game_dict[opponent] + game_dict[me]) %3 + 1 + {'X':0, 'Y':3, 'Z':6}[me]


part1_sum = part2_sum = 0
for line in input.splitlines():
    opponent, me = line.split(" ")
    part1_sum += game(opponent, me)
    part2_sum += game2(opponent, me)

print(part1_sum, part2_sum)
