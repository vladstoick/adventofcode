#include <fstream>
#include <stack>
#include <vector>
#include <iostream>

void PrintDebug(std::vector<std::stack<char>> items)
{
    for (int i = 0; i < items.size(); i++)
    {
        std::cout << "Item " << i;
        std::stack<char> copy = items[i];
        while (copy.size())
        {
            std::cout << "[" << copy.top() << "]";
            copy.pop();
        }
        std::cout << std::endl;
    }
}

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    std::stack<std::string> rows;
    while (std::getline(infile, line))
    {
        if (line[1] == '1')
        {
            break;
        }
        rows.push(line);
    }

    int itemsCount = (rows.top().size() + 1) / 4;

    std::vector<std::stack<char>> items(itemsCount);
    std::vector<std::stack<char>> itemsPart2(itemsCount);

    while (rows.size())
    {
        std::string row = rows.top();
        rows.pop();

        for (int i = 0; i < itemsCount; i++)
        {
            char c = row[i * 4 + 1];
            if (c != ' ')
            {
                items[i].push(c);
                itemsPart2[i].push(c);
            }
        }
    }

    PrintDebug(items);

    std::string word;

    while (infile >> word)
    {
        infile >> word;
        int countToMove = std::stoi(word);
        infile >> word;
        infile >> word;
        int from = std::stoi(word) - 1;
        infile >> word;
        infile >> word;
        int target = std::stoi(word) - 1;

        std::cout << "Moving " << countToMove << " from " << from << " to " << target << std::endl;

        int cp = countToMove;
        while (countToMove)
        {
            countToMove--;
            char toMove = items[from].top();
            items[from].pop();
            items[target].push(toMove);
        }

        std::vector<char> toMovePart2;
        countToMove = cp;
        while (countToMove)
        {
            countToMove--;
            toMovePart2.push_back(itemsPart2[from].top());
            itemsPart2[from].pop();
        }
        for(int i = toMovePart2.size() - 1; i >= 0; i--) {
            itemsPart2[target].push(toMovePart2[i]);
        }
    }

    PrintDebug(items);
    PrintDebug(itemsPart2);

    // Part1;
    std::cout << "Part1: ";
    for (int i = 0; i < itemsCount; i++)
    {
        std::cout << items[i].top();
    }
    std::cout << std::endl;

    // Part1;
    std::cout << "Part2: ";
    for (int i = 0; i < itemsCount; i++)
    {
        std::cout << itemsPart2[i].top();
    }
    std::cout << std::endl;

    return 0;
}