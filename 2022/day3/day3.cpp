#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    int part1 = 0;
    int part2 = 0;
    int x = 0;

    std::set<char> current;

    while (std::getline(infile, line))
    {
        int size = line.size();

        std::set<char> presentInFirstHalf;

        for (int i = 0; i < size / 2; i++)
        {
            presentInFirstHalf.insert(line[i]);
        }

        for (int i = size / 2; i < size; i++)
        {
            if (presentInFirstHalf.contains(line[i]))
            {
                int points = (line[i] >= 'a' && line[i] <= 'z' ? (line[i] - 'a') : (line[i] - 'A' + 26)) + 1;
                std::cout << x << "Found " << line[i] << " " << points << "\n";

                part1 += points;
                break;
            }
        }

        std::set<char> newPart2;
        for (int i = 0; i < size; i++)
        {
            newPart2.insert(line[i]);
        }
        if (current.size() == 0)
        {
            current = newPart2;
        }
        else
        {
            std::set<char> intersection;
            std::set_intersection(current.begin(), current.end(), newPart2.begin(), newPart2.end(), std::inserter(intersection, intersection.begin()));
            current = intersection;
        }

        if (x % 3 == 2)
        {
            char badge = *current.begin();
            int points = (badge >= 'a' && badge <= 'z' ? (badge - 'a') : (badge - 'A' + 26)) + 1;
            std::cout << x << "Found badge " << badge << " " << points << "\n";
            part2 += points;
            current = {};
        }

        x++;
    }

    std::cout << "Part 1 " << part1 << "\n";
    std::cout << "Part 2 " << part2 << "\n";

    return 0;
}