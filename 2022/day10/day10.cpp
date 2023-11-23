#include <iostream>
#include <fstream>
#include <string>

void printDebug(int sum, int cycle, int adding)
{
    std::cout << "At cycle " << cycle << " the sum is " << sum << " after adding " << adding << std::endl;
}

using matrix = std::vector<std::vector<bool>>;

void printMatrix(matrix display)
{
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 40; j++)
        {
            std::cout << (display[i][j] ? '#' : '.');
        }
        std::cout << std::endl;
    }
}

void processCycle(int cycle, int x, matrix &display)
{
    int cyclePosition = (cycle - 1) % 40;
    int spritePosition = x % 40;

    if (cyclePosition >= spritePosition - 1 && cyclePosition <= spritePosition + 1)
    {
        display[cycle / 41][cyclePosition] = true;
    }
}

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    int cycle = 1;
    int x = 1;
    int sum = 0;
    matrix display(6, std::vector<bool>(41, false));
    while (std::getline(infile, line))
    {
        processCycle(cycle, x, display);

        if ((cycle + 20) % 40 == 0)
        {
            int cycleRoundedUp = cycle;
            int adding = (cycleRoundedUp)*x;
            sum += adding;
            printDebug(sum, cycleRoundedUp, adding);
        }

        if (line[0] == 'n')
        {
            cycle++;
        }
        else
        {
            std::cout << cycle << " " << line << std::endl;
            // if it's 19, then nothing changes in this cycle and the next;
            if ((cycle + 20) % 40 == 39)
            {
                int cycleRoundedUp = cycle + 1;
                int adding = (cycleRoundedUp)*x;
                sum += adding;
                std::cout << "Adding early at cycle" << cycle << std::endl;
                printDebug(sum, cycleRoundedUp, adding);
            }
            processCycle(cycle + 1, x, display);
            x += std::stoi(line.substr(line.find(" ") + 1));
            cycle += 2;
        }
    }

    printMatrix(display);

    std::cout << sum;

    return 0;
}