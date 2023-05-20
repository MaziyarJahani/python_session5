def diamond(n):
    for a in range(n):
        for b in range(n - a - 1):
            print(" ", end="")
        for b in range(2 * a + 1):
            print("*", end="")
        print()
    for a in range(n - 2, -1, -1):
        for b in range(n - a - 1):
            print(" ", end="")
        for b in range(2 * a + 1):
            print("*", end="")
        print()
diamond(int(input()))
