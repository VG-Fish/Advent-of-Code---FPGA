direction_sign: dict[str, int] = {"L": -1, "R": 1}

def main():
    current: int = 50
    res: int = 0
    with open("input.txt", "r") as f:
        for line in f:
            direction: str = line[0]
            distance: int = int(line[1:])
            current = (direction_sign[direction] * distance + current) % 100
            if current == 0:
                res += 1
    print(res)


if __name__ == "__main__":
    main()
