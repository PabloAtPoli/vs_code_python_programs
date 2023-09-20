# importing package
import numpy

# define the polynomials
# p(x) = 5(x**2) + (-2)x +5

px = (5, -2, 5)

# q(x) = 2(x**2) + (-5)x +2
qx = (2, -5, 2)

# mul the polynomials
rx = numpy.polynomial.polynomial.polymul(px, qx)

# print the resultant polynomial
print("The result of the polynomial multiplication is... ")
print(rx)
print()

# add the polynomials
poly_addition = numpy.polynomial.polynomial.polyadd(px, qx)
print("The result of the polynomial addition is... ")
print(poly_addition)
print()

# subtract the polynomials
poly_subtraction = numpy.polynomial.polynomial.polysub(px, qx)
print("The result of the polynomial subtraction is... ")
print(poly_subtraction)
print()

# divide the polynomials
poly_division = numpy.polynomial.polynomial.polydiv(px, qx)
print("The result of the polynomial division is... ")
print(poly_division)
print()





