#include <iostream>
#include <fstream>
#include <cassert>
#include <tuple>

class Item
{
public:
    virtual std::string toString() = 0;
};

class Value : public Item
{
public:
    Value(int valueIn) : value(valueIn){};

    std::string toString()
    {
        return std::to_string(value);
    }

    int value;
};

enum Comparison
{
    Smaller,
    Equal,
    Greater
};

class List : public Item
{
public:
    List(std::vector<std::variant<List, Value>> itemsIn) : items(itemsIn)
    {
    }

    Comparison compare(List other)
    {

        for (int i = 0; i < items.size() && i < other.items.size(); i++)
        {
            auto thisItem = items[i];
            auto otherItem = other.items[i];

            bool isValueThis = std::holds_alternative<Value>(thisItem);
            bool isValueOther = std::holds_alternative<Value>(otherItem);

            if (isValueThis && isValueOther)
            {
                if (std::get<Value>(thisItem).value > std::get<Value>(otherItem).value)
                {
                    return Greater;
                }
                if (std::get<Value>(thisItem).value < std::get<Value>(otherItem).value)
                {
                    return Smaller;
                }
            }
            else
            {
                List newThisItem = isValueThis ? List({thisItem}) : std::get<List>(thisItem);
                List newOtherItem = isValueOther ? List({otherItem}) : std::get<List>(otherItem);
                auto comparison = newThisItem.compare(newOtherItem);
                if (comparison == Smaller)
                {
                    return Smaller;
                }
                else if (comparison == Greater)
                {
                    return Greater;
                }
            }
        }

        if (items.size() < other.items.size())
        {
            return Smaller;
        }
        else if (items.size() == other.items.size())
        {
            return Equal;
        }
        else
        {
            return Greater;
        }
    }

    std::string toString()
    {
        std::string result = "[";
        bool first = true;
        for (auto item : items)
        {
            if (!first)
            {
                result += ",";
            }
            first = false;
            result += std::visit([](auto &&arg)
                                 { return arg.toString(); },
                                 item);
        }
        result += "]";
        return result;
    }
    std::vector<std::variant<List, Value>> items;
};

struct Result
{
    List list;
    int endIndex;

    Result(List listIn, int endIndexIn) : list(listIn), endIndex(endIndexIn) {}
};

Result parseInput(std::string input, int idx)
{
    std::vector<std::variant<List, Value>> items;

    assert(input[idx] == '[');
    idx++;

    while (input[idx] != ']')
    {
        if (input[idx] == ',')
        {
            idx++;
        }
        else if (input[idx] >= '0' && input[idx] <= '9')
        {
            int number = input[idx] - '0';
            idx++;
            if (input[idx] >= '0' && input[idx] <= '9')
            {
                number = number * 10 + (input[idx] - '0');
            }

            items.push_back(Value(number));
        }
        else
        {
            auto result = parseInput(input, idx);
            items.push_back(result.list);
            idx = result.endIndex;
        }
    }

    auto list = List(items);
    return Result(list, idx + 1);
}

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    int part1 = 0;
    int index = 1;
    std::vector<List> lists;
    while (std::getline(infile, line))
    {
        auto [left, _idxLeft] = parseInput(line, 0);
        lists.push_back(left);
        std::cout << left.toString() << std::endl;

        std::getline(infile, line);
        auto [right, _idxRight] = parseInput(line, 0);
        lists.push_back(right);
        std::cout << right.toString() << std::endl;

        auto comparison = left.compare(right);

        if (comparison == Smaller)
        {
            std::cout << "Left < Right";
            part1 += index;
        }
        else if (comparison == Equal)
        {
            std::cout << "Left == Right";
        }
        else
        {
            std::cout << "Left > Right";
        }
        std::cout << std::endl;

        std::getline(infile, line);
        index++;

        std::cout << std::endl;
    }

    std::cout << "Part 1: " << part1 << std::endl;

    auto distress1 = List({List({2})});
    lists.push_back(distress1);
    auto distress2 = List({List({6})});
    lists.push_back(distress2);

    std::sort(lists.begin(), lists.end(), [](List &l, List &r)
              { return l.compare(r) == Smaller; });

    int part2 = 1;

    for (int i = 0; i < lists.size(); i++)
    {
        auto list = lists[i];
        std::cout << list.toString() << std::endl;

        if (list.compare(distress1) == Equal)
        {
            part2 *= (i + 1);
        }
        else if (list.compare(distress2) == Equal)
        {
            part2 *= (i + 1);
        }
    }

    std::cout << "Part 2: " << part2 << std::endl;

    return 0;
}