import sympy as sym

ACCEPTABLE_ERR = 1e-6


def get_lagrange_derivatives(points):
    derivatives = []
    for (i, point_i) in enumerate(points):
        coeff = "1"
        for (j, point_j) in enumerate(points):
            if (i==j):
                continue
            coeff += f"*(x - {point_j})/({point_i} - {point_j})"
        coeff_func = sym.sympify(coeff)
        derivatives.append(sym.Derivative(coeff_func, 'x').doit())
    return derivatives


def get_function_derivatvie(lagrange_derivatives, values):
    derivative = sym.sympify("0")
    for (i, d) in enumerate(lagrange_derivatives):
        derivative += d * values[i]
    return derivative


def get_derivative_values(derivative, points):
    values = []
    for point in points:
        values.append(derivative.subs({"x": point}))
    return values


def check_equality(values):
    for i in range(len(values) - 1):
        diff = values[i] - values[i+1]
        if diff > ACCEPTABLE_ERR or diff < -ACCEPTABLE_ERR:
            return False
    return True


def main():
    #get input
    n = int(input())
    points_string = input().split(" ")
    points = [float(point) for point in points_string]
    values_string = input().split(" ")
    values = [float(value) for value in values_string]
    #calculate the derivative at the given points and check if they're equal
    #repeat and increase the degree at each stage
    degree = 0
    while not check_equality(values):
        degree += 1
        lagrange_derivatives = get_lagrange_derivatives(points)
        derivative = get_function_derivatvie(lagrange_derivatives, values)
        values = get_derivative_values(derivative, points)
    print(degree)


if __name__ == "__main__":
    main()