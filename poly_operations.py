# importing package
import numpy

def print_polynomial(list_coeff):
    """
    This function prints the polynomial in a readable format.
    """

    i = len(list_coeff)-1
    pol_str =""
    while i >=0:
        if list_coeff[i] >0:
            if len(list_coeff) - i != 1:
                pol_str += " + "
        elif list_coeff[i] <0:
            pol_str += " - "
        if list_coeff[i] !=0:
            pol_str += str(abs(list_coeff[i])) + "X**" + str(i)
        i = i-1
    return pol_str


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
quotient, remainder = numpy.polynomial.polynomial.polydiv(px, qx)
print("The result of the polynomial division is... ")
print(f"Quotient = {quotient}")
print(f"Remainder = {remainder}")

# p(x) = 4(x**3) + 0x**2 + 3x - 8
px = (-8, 3, 0, 4)

# q(x) = x + 2
qx = (2, 1, 0)

print("p(x) = ", print_polynomial(px))
print("q(x) = ", print_polynomial(qx))



# divide the polynomials
quotient, remainder = numpy.polynomial.polynomial.polydiv(px, qx)
print("The result of the polynomial division is... ")
print(f"Quotient = {print_polynomial(quotient)}")
print("Remainder = ",print_polynomial(remainder) + " / " + print_polynomial(qx) )






