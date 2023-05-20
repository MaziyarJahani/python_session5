import math
# a * x + b = 0
a = int(input())
b = int(input())
x = -b / a
print (x)
c = int(input())
# a*x**2 + b*x + c = 0
Δ = b**2 - 4*a*c
if Δ > 0:
    x1 = (-b - math.sqrt(Δ)) / (2*a)
    x2 = (-b + math.sqrt(Δ)) / (2*a)
    print (x1 , x2)
elif Δ == 0:
    #/ is in same position as *. it reads from left to right
    x = -b/(2*a)
    print(x)
elif Δ < 0:
    print("no answer")
