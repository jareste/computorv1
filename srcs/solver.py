import re
import math, cmath

def _sqrt(number, isnegative, guess=0.0,):
    if guess == 0.0:
        guess = number / 2.0

    better_guess = (guess + number / guess) / 2.0

    if abs(guess - better_guess) < 0.000001:
        if isnegative:
            return complex(0, better_guess)
        return better_guess

    # Otherwise, use the better guess as the new guess and try again.
    else:
        return _sqrt(number, isnegative, better_guess)



def solve_equation(equation):
    coefficients = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', equation)]
    if len(coefficients) == 2:
        a, b = coefficients
        if a == 0:
            if b == 0:
                print("Infinite solutions")
                return None
            else:
                print("No solution")
                return None
        else:
            info = "Linear equation. The solution is:"
            print(info)
            return -b/a
    elif len(coefficients) == 3:
        a, b, c = coefficients
        print('a: ' + str(a))
        print('b: ' + str(b))
        print('c: ' + str(c))
        discriminant = b**2 - 4*a*c
        print('discriminant: ' + str(discriminant))
        if discriminant < 0:
            info = "Discriminant is strictly negative, the two complex solutions are:"
            print(info)
            # root1 = (-b + _sqrt(-discriminant, True)) / (2*a)
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - _sqrt(-discriminant, True)) / (2*a)
            print('root1: ' + str(root1))
            print('root2: ' + str(root2))
            root1 = str(root1).replace('j', 'i')
            root2 = str(root2).replace('j', 'i')
            return root1, root2
        elif discriminant == 0:
            info = "Discriminant is zero, the solution is:"
            print(info)
            return -b / (2*a)
        else:
            info = "Discriminant is strictly positive, the two real solutions are:"
            print(info)
            root1 = (-b + _sqrt(discriminant, False)) / (2*a)
            root2 = (-b - _sqrt(discriminant, False)) / (2*a)
            return root1, root2

    else:
        return "Equation degree is not 1 or 2"

# Test the function
# print(solve_equation("2 + 3"))  # Linear equation
# print(solve_equation("1+0+4"))  # Quadratic equation
