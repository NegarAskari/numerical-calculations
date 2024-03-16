import sympy as sym
from numpy import round


def get_uniform_points(a, b, n):
    points = []
    for k in range(n):
        points.append(a + ((b-a) * k / (n - 1)))
    return points


def get_chebyshev_points(a, b, n):
    points = []
    func = sym.sympify("(a+b)/2 + ((b-a)*cos((2*k+1)*pi/(2*n)))/2")
    func = func.subs({"a":a, "b":b, "n":n})
    for k in reversed(range(n)):
        points.append(func.subs("k", k).evalf())
    return points


def get_func_values(points, func):
    values = dict()
    for point in points:
        values[point] = func.subs('x', point)
    return values


def get_newton_coefficients(points, values):
    coefficients = []
    prev = []
    for point in points:
        current = [(values[point], point)]
        for p in prev:
            current.append((((current[-1][0] - p[0]) / (point - p[1])), p[1]))
        coefficients.append(float(current[-1][0]))
        prev = current
    return coefficients


def get_approximation(newton_coefficients, points, eval_point):
    sum = 0
    mult = 1
    for i, c in enumerate(newton_coefficients):
        sum += mult * c
        mult *= eval_point - points[i]
    return float(sum)


def main():
    #get input
    func = sym.sympify(input())
    points_string = input().split(" ")
    a = float(points_string[0])
    b = float(points_string[1])
    eval_point = float(input())
    n = int(input())
    #calculate chebyshev and uniform points
    chebyshev_points = get_chebyshev_points(a, b, n)
    uniform_points = get_uniform_points(a, b, n)
    #calculate the function at these points
    values = get_func_values(chebyshev_points + uniform_points, func)
    #calculate newton coefficients for each set of points
    chebyshev_coeffs = get_newton_coefficients(chebyshev_points, values)
    uniform_coeffs = get_newton_coefficients(uniform_points, values)
    #approximate the function according to each set (using newton method)
    chebyshev_approximation = get_approximation(chebyshev_coeffs, chebyshev_points, eval_point)
    uniform_approximation = get_approximation(uniform_coeffs, uniform_points, eval_point)
    #print the approximations and their difference
    print(round(chebyshev_approximation, 3))
    print(round(uniform_approximation, 3))
    print(abs(round((uniform_approximation - chebyshev_approximation), 3)))


if __name__ == "__main__":
    main()