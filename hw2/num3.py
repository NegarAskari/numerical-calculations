import sympy as sym
import numpy as np
from sympy.utilities.lambdify import lambdify


def find_maximum(func, a, b):
    derivative = sym.Derivative(func, "t").doit()
    solutions = sym.solve(derivative, "t")
    maximum = max(func.subs({"t": a}), func.subs({"t": b}))
    for solution in solutions:
        if solution >= b or solution <= a:
            continue
        maximum = max(func.subs({"t": solution}), maximum)
    return maximum


def find_ratio(a, b, maximum, func, n):
    x = a + (b - a) * np.random.random_sample(n)
    y = maximum * np.random.random_sample(n)
    f = lambdify("t", func, 'numpy')
    h = f(x)
    return sum(h >= y) / n


def main():
    #get input
    func = sym.sympify(input())
    n = int(input())
    a_b = input().split(" ")
    a = float(a_b[0])
    b = float(a_b[1])
    #find the maximum value of the function in the range [a, b]
    maximum = find_maximum(func, a, b)
    #find the random points and the ratio of random points inside the function
    ratio = find_ratio(a, b, maximum, func, n)
    #print the ratio times the area of the rectangle
    print(np.round(float(ratio * (b - a) * maximum), 2))


if __name__ == "__main__":
    main()