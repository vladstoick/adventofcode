#include <fstream>
#include <string>
#include <set>
#include <iostream>

int main()
{
    std::ifstream infile("input.txt");
    std::string line;
    std::getline(infile, line);

    for (int i = 4; i < line.size(); i++)
    {
        std::string code = line.substr(i - 4, 4);

        std::set<char> codeSet(code.begin(), code.end());
        if (codeSet.size() == 4)
        {
            std::cout << "Found at " << i << " in " << code << std::endl;
            break;
        }
    }

    for (int i = 14; i < line.size(); i++)
    {
        std::string code = line.substr(i - 14, 14);
        std::cout << code << " ";

        std::set<char> codeSet(code.begin(), code.end());
        if (codeSet.size() == 14)
        {
            std::cout << "Found at " << i << " in " << code << std::endl;
            break;
        }
    }

    return 0;
}