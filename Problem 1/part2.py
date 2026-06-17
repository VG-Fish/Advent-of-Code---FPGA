def main():
    current: int = 50
    res: int = 0
    with open("input.txt", "r") as f:
        for line in f:
            direction: int = -1 if line[0] == "L" else 1
            distance: int = int(line[1:])
            current = (direction * distance + current) % 100
            if current == 0:
                res += 1
    print(res)


if __name__ == "__main__":
    main()
