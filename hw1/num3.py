import sympy as sym
from numpy import round
from math import factorial


def get_kth_derivatives(func, k):
    x_derivates = [func]
    for i in range(k):
        x_derivates.append(sym.Derivative(x_derivates[-1], 'x').doit())
    derivatives = []
    for i, d in enumerate(x_derivates):
        derivative = d
        for j in range(k-i):
            derivative = sym.Derivative(derivative, 'y').doit()
        derivatives.append(derivative)
    return derivatives


def get_kth_taylor(func, a, b, x, y, k):
    derivates = get_kth_derivatives(func, k)
    sum = 0
    for i, d in enumerate(derivates):
        v = d.subs({'x': a, 'y': b})
        v *= (x-a)**i * (y-b)**(k-i)
        v *= factorial(k) / (factorial(i) * factorial(k-i) * factorial(k))
        sum += v
    return sum
   

def get_taylor_approximation(func, a, b, x, y, n):
    sum = 0
    for i in range(n+1):
        sum += get_kth_taylor(func, a, b, x, y, i)
    return float(sum)


def main():
    #get input
    func = sym.sympify(input())
    a_b = input().split(" ")
    a = float(a_b[0])
    b = float(a_b[1])
    x_y = input().split(" ")
    x = float(x_y[0])
    y = float(x_y[1])
    n = int(input())
    #calculate and print taylor approximation
    taylor_approximation = get_taylor_approximation(func, a, b, x, y, n)
    print(round(taylor_approximation, 4))
    #calculate and print actual function value
    value = float(func.subs({'x': x, 'y': y}))
    print(round(value, 4))


if __name__ == "__main__":
    main()