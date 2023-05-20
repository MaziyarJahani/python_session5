def multiplication_table(n, m):
    for a in range(1, n+1):
        for b in range(1, m+1):
            print(a * b, end="\t")
        print()
multiplication_table(int(input("please enter length:")), int(input("please enter width:")))