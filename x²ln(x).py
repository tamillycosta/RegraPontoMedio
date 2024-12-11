import math


def f(x):
    return x**2 * math.log(x)


def midpoint_rule(a, b, n):
    """
    Calcula a integral aproximada da função f(x) no intervalo [a, b]
    usando a Regra do Ponto Médio com n subintervalos.

    Args:
        a (float): limite inferior da integração.
        b (float): limite superior da integração.
        n (int): número de subintervalos.

    Returns:
        float: valor aproximado da integral.
    """
    h = (b - a) / n  
    integral = 0

    for i in range(n):
      
        mid = a + (i + 0.5) * h
        integral += f(mid)

    return integral * h

a = 1 
b = 2
n = 10 

result = midpoint_rule(a, b, n)
print(f"A integral aproximada de x^2 ln(x) no intervalo [{a}, {b}] é: {result}")