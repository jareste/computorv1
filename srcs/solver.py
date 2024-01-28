import re
import math, cmath

def solve_equation(equation):
    coefficients = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', equation)]
    print('coefficients: ' + str(coefficients[0]) + 'x^2 ' + str(coefficients[1]) + 'x ' + str(coefficients[2]))
    # Solve linear equation
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
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
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
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return root1, root2

    else:
        return "Equation degree is not 1 or 2"

# Test the function
# print(solve_equation("2 + 3"))  # Linear equation
# print(solve_equation("1+0+4"))  # Quadratic equation
