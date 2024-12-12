import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def f(x):
    return x**2 * np.log(x)

def midpoint_rule_with_plot(a, b, n):
    h = (b - a) / n  
    x_mid = [] 
    y_mid = [] 

    for i in range(n):
        mid = a + (i + 0.5) * h
        x_mid.append(mid)
        y_mid.append(f(mid))

    return x_mid, y_mid, h

a = 1  # Limite inferior
b = 2  # Limite superior
n = 10  # Número de subintervalos

x_mid, y_mid, h = midpoint_rule_with_plot(a, b, n)

x = np.linspace(a, b, 500)  
y = f(x)  

plt.figure(figsize=(10, 6))


plt.plot(x, y, label=r"$x^2 \ln(x)$", color="blue")


for i in range(n):
    plt.bar(x_mid[i], y_mid[i], width=h, align='center', edgecolor='black', color='orange', alpha=0.6)

plt.title("Regra do Ponto Médio: Aproximação da Integral", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.legend()
plt.grid(alpha=0.4)

# Mostrando o gráfico
plt.show()
