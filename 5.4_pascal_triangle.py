def pascal_triangle(n):
    triangle = [[1] * (a+1) for a in range(n)]
    for a in range(2, n):
        for b in range(1, a):
            triangle[a][b] = triangle[a-1][b-1] + triangle[a-1][b]
    return triangle
n = int(input("enter your number:"))
result = pascal_triangle(n)
for row in result:
    for number in row:
        print(number, end=' ')
    print()