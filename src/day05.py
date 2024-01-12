import re

def solve(fn, part):
    with open(fn) as fn:
        crates, moves = fn.read().split("\n\n")

        crate_lines = crates.split("\n")
        crate_idx = {int(c): i for i, c in enumerate(crate_lines[-1]) if c.isdigit()}
        
        crates = {k: '' for k in crate_idx.keys()}
        
        for crate, idx in crate_idx.items():
            for line in reversed(crate_lines[:-1]):
                if (crate_contents := line[idx]) != ' ':
                    crates[crate] += crate_contents

        moves = [[int(i) for i in re.findall("(\\d+)",li)] for li in moves.split("\n")]

    for move in moves:
        num_crates, from_stack, to_stack = move
        crates_to_move = crates[from_stack][-num_crates:] # Get the topmost crates
        if part == 1:
            crates_to_move = crates_to_move[::-1]
        crates[from_stack] = crates[from_stack][:-num_crates]  # Remove from source stack
        crates[to_stack] += crates_to_move  # Add to destination stack

    # Step 3: Retrieve the topmost crate from each stack
    topmost_crates = [crates[i][-1] if crates[i] else '' for i in range(1,10)]

    print("".join(topmost_crates))


solve("inputs/day5.txt", part=1)
solve("inputs/day5.txt", part=2)