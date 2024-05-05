# HW2
## num1
This exercise is about using numerical differentiation to approximate the degree of a polynomial. The derivative is calculated as follows:
```math
f'(x_j)≈\sum_{k=0}^{n} f(x_k) L'_k(x_j)
```
Where $L_k$ denotes the lagrange coefficient.
### inputs:
The first line of the input is the number of points where we have evaluated the function.
The second and third line consist of the x and y values of these points, respectively. 
### outputs:
The output shows the approximated degree of the polynomial.
### example input and output
input:
```
6
1 3 4 7 9 11
3 27 48 147 243 363
```
output:
```
2
```
## num2
This exercise is about composite numerical differentiation methods, namely: intermediate point, rectangle, trapezoid and simpson.
These integrals are calculated as follows:
```math
x_i = a + (i - 1/2)h
```
```math
I_i = h \sum_{i=1}^{n} f(x_i)
```
```math
x_i = a + ih
```
```math
I_r = h \sum_{i=0}^{n-1} f(x_i)
```
```math
I_t = \frac{h}{2} \sum_{i=0}^{n-1} (f(x_i) + f(x_{i+1}))
```
```math
I_s = \frac{h}{3} \sum_{i=1}^{n/2} (f(x_{2i-2}) + 4f(x_{2i-1}) + f(x_{2i}) )
```
### inputs:
The first line of the input contains an analytical function, the second line is the number of sections the integral will be calculated on.
The third line, contains the bounds of the integral.
### outputs:
The output includes the integral calculated by various methods and their respective errors.
### example intput and output
input:
```
100 * sin(x) + 12 * (x ** 2) * cos(x)
9
3 7
```
output:
```
248.543 133.689
382.201 0.031
382.276 0.044
382.226 0.006
```
## num3
This exercise is about the Monte Carlo numerical integral method.
In this method, we encapsulate the function in a rectangle, select a number of random points within that rectangle, and note the ratio of points that end up within the function.
The approximate value of the integral equals the area of the rectangle multiplied by this ratio.
### inputs:
The first line of the input contains an analytical function, the second line notes the number of random points to use, and the third line includes the bounds of the integral.
### outputs:
The output contains the approximated integral value.
### example input and output
input:
```
sin(t)
100000
0 3.14
```
output:
```
2.0
```
