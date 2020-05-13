""""
File: quadratic_solver.py
This program solves the quadratic equation
"""

import math


def main():
    print('Welcome to Quadratic Equation Solver!')
    print('This program solves equation of the form Ax^2 +Bx +C = 0')
    A = float(input('Enter the coefficient A: '))
    B = float(input('Enter the coefficient B: '))
    C = float(input('Enter the coefficient C: '))
    discriminant = (B ** 2) - (4 * A * C)
    if discriminant < 0:
        discriminant *= -1
        first_term, second_term = solve_equation(A, B, discriminant)
        print('The roots of ' + str(A) + ' x^2 + ' + str(B) + ' x ' + str(C) + ' = 0 are:')
        print('x1 = ' + str(first_term) + ' + i' + str(second_term) + '\n x2 = ' + str(first_term) + ' - i' + str(second_term))
    else:
        first_term, second_term = solve_equation(A, B, discriminant)
        print('The roots of ' + str(A) + ' x^2 + ' + str(B) + ' x ' + str(C) + ' = 0 are:')
        print('x1 = ' + str(first_term + second_term) + '\n x2 = i' + str(first_term - second_term))


def solve_equation(a, b, discriminant):
    first_term = -b / (2 * a)
    second_term = discriminant / (2*a)

    return first_term, second_term


if __name__ == '__main__':
    main()
