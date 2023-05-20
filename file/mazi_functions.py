import math

def say_hello(name):
    print("hello", name)

def say_goodbye():
    print("bye bye")

def second_degree_equation (a , b , c):
    if type(a) == int and type(b) == int and type(c) == int:
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
#def second_degree_equation (a: int , b: int , c: int):