#include <computor.h>

int main(int ac, char **av)
{
	std::vector<std::string> parsed;

	if (ac == 1)
		std::cerr << "Please introduce more than one argument." << std::endl;
	try
	{
		parsed = parse(av);
	}
	catch (std::invalid_argument &e)
	{
		std::cerr << e.what() << std::endl;
		return (1);
	}
	solver(parsed);
	// tokens = tokenize(av);

	return (0);
}
