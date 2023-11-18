#include <fstream>
#include <string>
#include <tuple>
#include <iostream>

using pair = std::tuple<int, int>;

pair parsePair(std::string input)
{
    int first = std::stoi(input.substr(0, input.find("-")));
    int second = std::stoi(input.substr(input.find("-") + 1, input.size()));

    return std::make_tuple(first, second);
}

bool match(pair first, pair second) {
    if(std::get<0>(first) > std::get<0>(second)) {
        auto aux = first;
        first = second;
        second = aux;
    }

    if(std::get<0>(first) == std::get<0>(second)) {
        return true;
    }

    return std::get<1>(first) >= std::get<1>(second);
}

bool overlaps(pair first, pair second) {
    if(std::get<0>(first) > std::get<0>(second)) {
        auto aux = first;
        first = second;
        second = aux;
    }

    if(std::get<0>(first) == std::get<0>(second)) {
        return true;
    }

    return std::get<1>(first) >= std::get<0>(second);

}

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    int part1 = 0;
    int part2 = 0;

    while (std::getline(infile, line))
    {
        pair firstPair = parsePair(line.substr(0, line.find(",")));
        pair secondPair = parsePair(line.substr(line.find(",") + 1, line.size()));

        bool matches = match(firstPair, secondPair);
        bool overlap = overlaps(firstPair, secondPair);
        std::cout << std::get<0>(firstPair) << " " << std::get<1>(firstPair);
        std::cout << ";" << std::get<0>(secondPair) << " " << std::get<1>(secondPair) << " ";
        std::cout << (matches ? "Mathces" : "Not Match");
        std::cout << (overlap ? "Mathces" : "Not Match");
        std::cout << std::endl;

        part1 += matches ? 1 : 0;
        part2 += overlap ? 1 : 0;
    }

    std::cout << "Part 1: " << part1;
    std::cout << "Part 2: " << part2;
}