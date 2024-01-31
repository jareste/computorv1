#include <computor.h>

bool is_sign(char c)
{
    if (c == '+' || c == '-' || c == '*' || c == '/' || c == '=')
        return (true);
    return (false);
}

static bool is_token(char c)
{
    if (is_sign(c) || isdigit(c) || c == '^' || c == '.'
        || c == 'x' || c == 'X')
        return (true);
    return (false);
}

static bool checkPrev(std::vector<std::string> parser, char c, bool space)
{
    int i = parser.size();
    if (i == 0)
        return (true);
    if (isdigit(c) && isdigit(parser[i - 1][0]) && space == true)
        return (false);
    if (c == '.' && !isdigit(parser[i - 1][0]))
        return (false);
    // std::cout << "checkPrev: " << c << " " << parser[i-1] << (c == 'X' && parser[i - 1] == "X") << std::endl;
    if (c == 'X' && parser[i - 1] == "X")
        return (false);
    return (true);
}

std::vector<std::string> parse(char **av)
{
    std::vector<std::string> parser;
    bool equalFound = false;
    bool space = false;
    bool xFound = false;

    for (int i = 1; av[i]; i++)
    {
        for(int j = 0; av[i][j]; j++)
        {
            if (av[i][j] == ' ')
            {
                space = true;
                continue ;
            }
            if (!is_token(av[i][j]))
                throw std::invalid_argument("Invalid token: " + std::string(1, av[i][j]));
            if (av[i][j] == '=' && equalFound == true)
                throw std::invalid_argument("Found more than one equal");
            else if (av[i][j] == '=')
                equalFound = true;
            if (av[i][j] == 'x')
                av[i][j] = 'X';
            if (!checkPrev(parser, av[i][j], space))
                throw std::invalid_argument("Invalid token: " + std::string(1, av[i][j]));
            parser.push_back(std::string(1, av[i][j]));
            space = false;
        }
    }

    for(int i = 0; i < int(parser.size()); i++)
    {
        if (parser[i] == "X")
            xFound = true;
        if (parser[i] == "=" || is_sign(parser[i][0]))
            std::cout << " ";
        std::cout << parser[i];
        if (parser[i] == "=" || is_sign(parser[i][0]))
            std::cout << " ";
    }
    std::cout << std::endl;
    if (!xFound)
        throw std::invalid_argument("No X found");
    if (!equalFound)
        throw std::invalid_argument("No equal found");
    // for (int i = 0; i < parser.size(); i++)
    // {
    //     if (parser[i] == "x" || parser[i] == "X")
    //     {
    //         if (i == 0 || parser[i - 1] == "+" || parser[i - 1] == "-" || parser[i - 1] == "*" || parser[i - 1] == "/"
    //             || parser[i - 1] == "^" || parser[i - 1] == "=")
    //             parser.insert(parser.begin() + i, "1");
    //         else if (parser[i - 1] == ".")
    //             parser.insert(parser.begin() + i, "0");
    //     }
    // }
    return parser;
}