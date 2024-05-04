# HW1
## num1
This exercise is about the Newton and Lagrange interpolation methods. For the Lagrange method we have:
```math
P_n(x)=\sum_{i=0}^{n} L_i(x)f(x_i)
```
And for the Newton method we have:
```math
P_n(x) = \sum_{i=0}^{n} f[x_0,...,x_i] \prod_{j=0}^{i-1} (x-x_j)
```
### inputs:
On the first line, we enter an analytical function. On the second line, the points we would like to use for interpolation, and on the third line the point at which we want to approximate the function.
### outputs:
On the first line, we print the Lagrange coefficients:
```math
L_i = \prod_{j=0, j \neq i}^{n} \frac{x-x_j}{x_i-x_j}
```
On the second line, we print the divided differences from the Newton interpolation method: (only the ones of the form $`f[x_0,...,x_k]`$)
```math
f[x_i,..., x_{i+k}] = \frac{f[x_{i+1},...,x_{i+k}]-f[x_i,...,x_{i+k-1}]}{x_{i+k}-x_i}
```
And finally, on the last line, we print the approximation calculated by interpolation.
### example input and output
input:
```
2.787*2.508**x + 0.798*x**2.515 + 3.389*sin(2.182*x)
10.5 10.6 6.8 6.2
5.4
```
output:
```
3.661 -3.416 -2.515 3.271
43751.257 41921.768 8030.457 1278.101
-4535.368
```
## num2
This exercise is about the Newton interpolation method on uniform/Chebyshev points. To get n uniform points in the range [a,b] we have:
```math
x_k = a + (b-a) \times \frac{k-1}{n-1} , k = 1,...,n
```
To get n Chebyshev points in the range [a,b] we have:
```math
x_k = \frac{1}{2}(a+b) + \frac{1}{2}(b-a)cos(\frac{2k-1}{2n}\pi), k=1,...,n
```
### inputs
On the first line, we enter an analytical function. On the second line, we enter the beginning and end of the range we would like to use for interpolation.
On the third line, we enter the point at which we would like to approximate the function. And, on the last line, we enter n, the number of points within the range that we get to use for interpolation.
### outputs
In the first two lines, we print the approximated value using the Chebychev and uniform points respectively. And, on the third line, we print the difference between these outputs.
### example input and output
input:
```
2.1*3.284**x
1.5 3.9
4.6
7
```
output:
```
496.572
496.411
0.161
```
## num3
This exercise is about Taylor's polynomial for a function of two variables. The polynomial of the n-th order is calculated as follows:
```math
P_n(x,y) = \sum_{i=0}^{n} \frac{1}{i!} ((x-a)\frac{\partial}{\partial x} + (y-b)\frac{\partial}{\partial y})^i f\vert_{a,b}
```
### inputs
On the first line, we enter an analytical function. On the second line, we enter points a and b around which we will calculate the polynomial.
On the third line, we enter points x and y at which we want to approximate the function. On the fourth line, we enter the order of the polynomial we want to calculate.
### outputs
In two lines, we print the approximated and exact value of the function at point (x,y).
### example input and output
input:
```
3.866*y**0.101 + 2.216*sin(4.099*x + 3.566*y) + 1.207
0.8 0.9
0.8 0.1
5
```
output:
```
3.04
3.2197
```
