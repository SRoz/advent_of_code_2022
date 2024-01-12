from dataclasses import dataclass
from typing import Any, Self

with open("inputs/day7_test.txt") as fn:
    input = fn.read()

lines = input.splitlines()

dir = ""

# @dataclass
# class File:
#     name: str
#     size: int

# @dataclass
# class Folder:
#     name: str
#     children: list[File | Self ]


@dataclass
class Terminal:
    mode: str # input / output
    current_dir: list[str]
    filesystem: dict[str, list]

    def fs_getter(self, key: list[str]):
        out = self.filesystem
        for k in key:
            out = out.get(k)
        return out

    def fs_setter(self, key: list[str], value: Any):
        folder = self.fs_getter(key[:-1])
        folder[key[-1]] = value

        # for 

    def input(self, line):
        match line.split(" "):
            case ["$", "cd", dir]:
                if dir[0:2] == '..':
                    self.current_dir = dir[:-1]
                elif dir[0] == '/':
                    self.current_dir = dir
                else:
                    self.current_dir[-1] = dir
                print("cd to", self.current_dir)
            
            case ["$", "ls"]:
                self.mode = 'LS'
                print("LS")
            
            case ["dir", dir]:
                print("DIR", dir)
                self.fs_[dir] = {}
            
            case [filesize, filename]:
                print(f"filesize: {filesize}, fn {filename}")
                self.current_dir[filename] = filesize

            case _:
                print("NA")
        
            
terminal = Terminal(mode='', current_dir=[], folders=[])

for line in lines:
    terminal.input(line)
