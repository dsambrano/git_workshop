from pathlib import Path
import time

intro_file = Path("hello_world.txt")
outro_file = Path("goodbye.txt")


with intro_file.open() as f:
    instructions = f.readline()

with outro_file.open() as f:
    debreif = f.readline()

def main():
    print(instructions)
    time.sleep(1)
    name = input("Enter Name:")
    print("Hello " + name)
    time.sleep(1)
    print(debreif)
