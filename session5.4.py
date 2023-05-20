# if you have cope_paste in command, you have a bad code.
import math
def second_degree_equation (a , b , c):
    #global a
    Δ = b**2 - 4*a*c
    if Δ > 0:
        x1 = (-b - math.sqrt(Δ)) / (2*a)
        x2 = (-b + math.sqrt(Δ)) / (2*a)
        print (x1 , x2)
    elif Δ == 0:
        x = -b/(2*a)
        print(x)
    elif Δ < 0:
        print("no answer")
        
second_degree_equation (3, 5, 6)
print("_______________")
t = int(input())
second_degree_equation (2, int(input()), t)
print("_______________")
#second_degree_equation (0 , 0 , 0)
# a should not be 0
second_degree_equation (1,0,0)