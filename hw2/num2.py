import sympy as sym
import numpy as np
from sympy.utilities.lambdify import lambdify
from numpy import round


def evaluate_function(a, b, h, func):
    f = lambdify("x", func, 'numpy')
    return f(np.arange(a, b + h, h))


def get_rectangle_integral(h, n, values):
    integral = 0
    for i in range(n):
        integral += h * values[2 * i]
    return integral


def get_intermediate_integral(h, n, values):
    integral = 0
    for i in range(n):
        integral += h * values[(2 * i) + 1]
    return integral


def get_trapezoid_integral(h, n, values):
    integral = 0
    for i in range(n):
        integral += h * 0.5 * (values[2 * i] + values[(2 * i) + 2])
    return integral


def get_simpson_integral(h, n, values):
    integral = 0
    for i in range(1, n, 2):
        integral += h * (values[i - 1] + values[i + 1] + (4 * values[i])) / 3
    return integral


def main():
    #get input
    func = sym.sympify(input())
    n = int(input())
    a_b = input().split(" ")
    a = float(a_b[0])
    b = float(a_b[1])
    #calculate the actual integral value and the length of each section
    integral = float(sym.integrate(func, ("x", a, b)))
    h = (b - a) / n
    #evaluate the function at the needed points
    values = evaluate_function(a, b, h/2, func)
    #calculate rectangle integral and its error
    rectangle_integral = float(get_rectangle_integral(h, n, values))
    rectangle_error = round(abs(rectangle_integral - integral), 3)
    print(round(rectangle_integral, 3), rectangle_error)
    #calculate intermediate integral and its error
    intermediate_integral = float(get_intermediate_integral(h, n, values))
    intermediate_error = round(abs(intermediate_integral - integral), 3)
    print(round(intermediate_integral, 3), intermediate_error)
    #calculate trapezoid integral and its error
    trapezoid_integral = float(get_trapezoid_integral(h, n, values))
    trapezoid_error = round(abs(trapezoid_integral - integral), 3)
    print(round(trapezoid_integral, 3), trapezoid_error)
    #calculate simpson integral and its error
    simpson_integral = float(get_simpson_integral(h/2, n*2, values))
    simpson_error = round(abs(simpson_integral - integral), 3)
    print(round(simpson_integral, 3), simpson_error)


if __name__ == "__main__":
    main()