def chessboard(n, m):
    for a in range(n):
        for b in range(m):
            if (a + b) % 2 == 0:
                print("#", end="")
            else:
                print("-", end="")
        print()
chessboard(int(input("please enter length:")), int(input("please enter width:")))