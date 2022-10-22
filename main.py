from pathlib import Path
import datetime
import time

intro_file = Path("instructions.txt")
outro_file = Path("goodbye.txt")
data_dir = Path("data")

if not data_dir.exists():
    data_dir.mkdir(parents=True, exist_ok=True)


with intro_file.open() as f:
    instructions = f.readlines()

with outro_file.open() as f:
    debreif = f.readlines()

def save_data(data: str) -> None:
    today = datetime.datetime.now()
    filename = f"{today.strftime('%m-%d-%Y_%H-%M')}.csv"
    data_file = data_dir / Path(filename)
    with data_file.open("w") as f:
        f.write(data)

def main():
    print(instructions)
    time.sleep(1)
    name = input("Enter Name:")
    print("Hello " + name)
    save_data(name)
    time.sleep(1)
    print(debreif)

if __name__ == "__main__":
    main()
