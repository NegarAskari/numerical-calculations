import sympy as sym
from numpy import round


def get_lagrange_coefficients(points, eval_point):
    coefficients = []
    for point1 in points:
        coeff = 1
        for point2 in points:
            if point1 == point2:
                continue
            coeff *= (eval_point - point2) / (point1 - point2)
        coefficients.append(coeff)
    return coefficients


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


def get_approximation(lagrange_coefficients, points, values):
    sum = 0
    for i, c in enumerate(lagrange_coefficients):
        sum += c * values[points[i]]
    return float(sum)


def main():
    #get input
    func = sym.sympify(input())
    points_string = input().split(" ")
    points = [float(point) for point in points_string]
    eval_point = float(input())
    #calculate and print lagrange coefficients
    lagrange_coefficients = get_lagrange_coefficients(points, eval_point)
    for c in lagrange_coefficients:
        print(round(c, 3), end=" ")
    #calculate function values at the given points
    values = get_func_values(points, func)
    #calculate and print newton coefficients
    newton_coefficients = get_newton_coefficients(points, values)
    print()
    for c in newton_coefficients:
        print(round(c, 3), end=" ")
    #calculate and print final approximation (using lagrange method)
    approximation = get_approximation(lagrange_coefficients, points, values)
    print()
    print(round(approximation, 3))
    
    


if __name__ == "__main__":
    main()