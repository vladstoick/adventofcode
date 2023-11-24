#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <sstream>

std::vector<long> processItemsString(std::string itemsString)
{
    itemsString = itemsString.substr(itemsString.find(": ") + 2);

    std::stringstream ss(itemsString);
    std::string temp;
    std::vector<long> items;

    while (std::getline(ss, temp, ','))
    {
        items.push_back(std::stoi(temp));
    }

    return items;
}
enum OperationType
{
    Multiply,
    Sum,
};

class Operation
{
public:
    Operation(std::string operationLine)
    {
        operationLine = operationLine.substr(operationLine.find('=') + 6);

        type = operationLine[0] == '*' ? Multiply : Sum;

        operationLine = operationLine.substr(2);
        value = operationLine == "old" ? -999 : std::stoi(operationLine);
    }

    long apply(int apply)
    {
        long valueToUse = (value == -999) ? apply : value;
        long finalValue = type == Multiply ? (valueToUse * apply) : (valueToUse + apply);

        return finalValue;
    }

private:
    OperationType type;
    int value;
};

int greatDivisibility = 1;

class Monkey
{
public:
    Monkey(
        std::vector<long> items,
        Operation operation,
        int divisibleBy,
        int monkeyTargetTrue,
        int monkeyTargetFalse) : items_(items),
                                 operation_(operation),
                                 divisibleBy_(divisibleBy),
                                 monkeyTargetTrue_(monkeyTargetTrue),
                                 monkeyTargetFalse_(monkeyTargetFalse)
    {
    };

    void process(std::vector<Monkey> &monkeys, int index, bool part1)
    {
        while (items_.size() != 0)
        {
            counted++;
            auto value = items_[0];

            value = operation_.apply(value);
            value = part1 ? (value / 3) : value;

            bool isDivisble = value % divisibleBy_ == 0;
            int target = isDivisble ? monkeyTargetTrue_ : monkeyTargetFalse_;

            items_.erase(items_.begin());
            monkeys[target].addItem(value);
        }
    }

    void addItem(long item)
    {
        items_.push_back(item % greatDivisibility);
    }

    long counted = 0;

private:
    std::vector<long> items_;
    Operation operation_;
    int divisibleBy_;
    int monkeyTargetTrue_;
    int monkeyTargetFalse_;
};

void processResult(std::vector<Monkey> monkeys, int part)
{
    std::priority_queue<long, std::vector<long>, std::greater<long>> minq;
    for (int i = 0; i < monkeys.size(); i++)
    {
        minq.push(monkeys[i].counted);
        if (minq.size() > 2)
        {
            minq.pop();
        }
    }

    long val = minq.top();
    minq.pop();
    long val2 = minq.top();
    std::cout << "Part " << part << ": " << val << " * " << val2 << " = " << val * val2 << std::endl;
}

int main()
{
    std::ifstream infile("input.txt");
    std::string line;
    std::vector<Monkey> monkeys;
    std::vector<Monkey> monkeys2;

    while (std::getline(infile, line))
    {
        // Items
        std::getline(infile, line);
        auto items = processItemsString(line);

        // Operation
        std::getline(infile, line);
        auto operation = Operation(line);

        // Divisible By
        std::getline(infile, line);
        int divisibleBy = std::stoi(line.substr(line.find("y") + 2));

        // Monkey target true
        std::getline(infile, line);
        int monkeyTargetTrue = std::stoi(line.substr(line.find("y") + 2));

        // Monkey taget false
        std::getline(infile, line);
        int monkeyTargetFalse = std::stoi(line.substr(line.find("y") + 2));

        // Empty line
        std::getline(infile, line);

        auto monkey = Monkey(items, operation, divisibleBy, monkeyTargetTrue, monkeyTargetFalse);
        auto monkey2 = Monkey(items, operation, divisibleBy, monkeyTargetTrue, monkeyTargetFalse);

        monkeys.push_back(monkey);
        monkeys2.push_back(monkey2);

        greatDivisibility *= divisibleBy;
    }

    for (int i = 0; i < 20; i++)
    {
        for (int i = 0; i < monkeys.size(); i++)
        {
            monkeys[i].process(monkeys, i, true);
        }
    }

    processResult(monkeys, 1);

    for (int i = 0; i < 10000; i++)
    {
        for (int i = 0; i < monkeys2.size(); i++)
        {
            monkeys2[i].process(monkeys2, i, false);
        }
    }

     processResult(monkeys2, 2);

    return 0;
}