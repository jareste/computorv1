#include <computor.h>

void solver(std::vector<std::string>  parser)
{
    double constant = 0;
    // double x = 0;
    // double x2 = 0;

    bool equalFound = false;
    int j = 0;
    for (int i = 0; i < int(parser.size()); i++)
    {
        if (parser[i] == "=")
        {
            equalFound = true;
            continue ;
        }
        j = 0;
        while ()
        // if (parser[i] == "=")
        // {
        //     equalFound = true;
        //     continue ;
        // }
        // if (equalFound == false)
        // {
        //     if (isdigit(parser[i][0]) && is_sign(parser[i - 1][0]))
        //     {
        //         switch (parser[i - 1][0])
        //         {
        //             case '+':
        //                 constant += std::stod(parser[i]);
        //                 break ;
        //             case '-':
        //                 constant -= std::stod(parser[i]);
        //                 break ;
        //             case '*':
        //                 constant *= std::stod(parser[i]);
        //                 break ;
        //             case '/':
        //                 constant /= std::stod(parser[i]);
        //                 break ;
        //         }
        //     std::cout << "constant: " << constant << std::endl;
        //     }
        // }
        // else
        // {
        //     if (isdigit(parser[i][0]) && is_sign(parser[i - 1][0]))
        //     {
        //         switch (parser[i - 1][0])
        //         {
        //             case '+':
        //                 constant -= std::stod(parser[i]);
        //                 break ;
        //             case '-':
        //                 constant += std::stod(parser[i]);
        //                 break ;
        //             case '*':
        //                 constant /= std::stod(parser[i]);
        //                 break ;
        //             case '/':
        //                 constant *= std::stod(parser[i]);
        //                 break ;
        //         }
        //     std::cout << "constant: " << constant << std::endl;
        //     }
        // }
        // std::cout << parser[i] << std::endl;
    }
    // print(constant);


}

// // Step 1: Simplify the equation
// double x_coefficient = 1 + 3; // Coefficient of X
// double x2_coefficient = -1; // Coefficient of X^2
// double constant = 3 - 5 - 9; // Constant term

// // Step 2: Move all terms to one side of the equation
// // The equation is already in the standard form ax^2 + bx + c = 0

// // Step 3: Solve the equation
// if (x2_coefficient != 0) {
//     // The equation is a second degree equation
//     // Use the quadratic formula to solve it
//     double discriminant = x_coefficient * x_coefficient - 4 * x2_coefficient * constant;
//     if (discriminant < 0) {
//         // The equation has no real solutions
//     } else {
//         // The equation has two real solutions
//         double root1 = (-x_coefficient + sqrt(discriminant)) / (2 * x2_coefficient);
//         double root2 = (-x_coefficient - sqrt(discriminant)) / (2 * x2_coefficient);
//     }
// } else if (x_coefficient != 0) {
//     // The equation is a first degree equation
//     // Use simple algebra to solve it
//     double root = -constant / x_coefficient;
// } else {
//     // The equation is a constant equation
//     if (constant == 0) {
//         // The equation is always true
//     } else {
//         // The equation is never true
//     }
// }