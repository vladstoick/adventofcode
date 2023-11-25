#include <iostream>
#include <fstream>
#include <sstream>
#include <set>

class Range
{
public:
    Range(int lIn, int rIn) : l(lIn), r(rIn) {}
    int l;
    int r;

    std::vector<Range> unionWithRange(Range rangeToAdd)
    {
        auto rangeL = *this;
        auto rangeR = rangeToAdd;

        if (rangeL.r < rangeR.l)
        {
            // no intersection
            return {};
        }
        else
        {
            return {Range(rangeL.l, std::max(rangeL.r, rangeR.r))};
        }
    }
};

class Ranges
{
public:
    Ranges(int index) : index_(index){};

    void addRange(Range rangeToAdd)
    {
        ranges.push_back(rangeToAdd);
        std::sort(ranges.begin(), ranges.end(), [](auto &lhs, auto &rhs)
                  { return lhs.l < rhs.l; });

        std::vector<Range> newRanges;
        newRanges.push_back(ranges[0]);

        for (int i = 1; i < ranges.size(); i++)
        {
            auto result = (newRanges[newRanges.size() - 1]).unionWithRange(ranges[i]);
            if (result.size() == 1)
            {
                newRanges[newRanges.size() - 1] = result[0];
            }
            else
            {
                newRanges.push_back(ranges[i]);
            }
        }

        ranges = newRanges;
    }
    std::vector<Range> ranges;

private:
    int index_;
};

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    int MAX_ROW = 4000000;
    int MIN_ROW = 0;
    // int MAX_ROW = 2753392;
    // int MIN_ROW = 2753392;
    int ROW_PART_1 = 2000000;
    std::vector<Ranges> rangesEliminated;
    for (int i = 0; i <= MAX_ROW; i++)
    {
        rangesEliminated.push_back(Ranges(i));
    }
    std::set<int> a;
    std::vector<std::set<int>> beaconOrSensor(MAX_ROW + 1, a);

    while (std::getline(infile, line))
    {
        std::stringstream ss(line);
        std::string temp;

        std::getline(ss, temp, '=');
        std::getline(ss, temp, ' ');
        int sensorX = std::stoi(temp.substr(0, temp.size() - 1));

        std::getline(ss, temp, '=');
        std::getline(ss, temp, ' ');
        int sensorY = std::stoi(temp.substr(0, temp.size() - 1));

        std::getline(ss, temp, '=');
        std::getline(ss, temp, ' ');
        int beaconX = std::stoi(temp.substr(0, temp.size() - 1));

        std::getline(ss, temp, '=');
        std::getline(ss, temp, ' ');
        int beaconY = std::stoi(temp);

        int distanceX = std::abs(sensorX - beaconX) + 1;
        int distanceY = std::abs(sensorY - beaconY) + 1;
        int totalDistance = distanceX + distanceY;

        for (int row = MIN_ROW; row <= MAX_ROW; row++)
        {

            int distanceToRow = std::abs(row - sensorY);
            int leftX = totalDistance - distanceToRow - 2;
            if (leftX > 0)
            {
                int l = sensorX - leftX;
                int r = sensorX + leftX;

                rangesEliminated[row].addRange(Range(l, r));
            }

            if (beaconY == row && beaconY >= MIN_ROW && beaconY <= MAX_ROW)
            {
                beaconOrSensor[row].insert(beaconX);
            }

            if (sensorY == row && row >= MIN_ROW && sensorY <= MAX_ROW)
            {
                beaconOrSensor[row].insert(sensorY);
            }
        }
    }

    std::cout << "Starting calculation of part 1 " << std::endl;
    std::set<int> pointsElimated;
    for (auto range : rangesEliminated[ROW_PART_1].ranges)
    {
        for (int j = range.l; j <= range.r; j++)
        {
            if (beaconOrSensor[ROW_PART_1].count(j) == 0)
            {
                pointsElimated.insert(j);
            }
        }
    }
    std::cout << "Part 1 : " << pointsElimated.size() << std::endl;

    for (int row = MIN_ROW; row <= MAX_ROW; row++)
    {
        if (row % 10000 == 0)
        {
            std::cout << row << std::endl;
        }

        int l = 0;

        for (auto range : rangesEliminated[row].ranges)
        {
            for (int j = l; j < std::max(range.l, 0); j++)
            {
                if (beaconOrSensor[row].count(j) == 0)
                {
                    long result = (long)j * 4000000 + row;
                    std::cout << "Part 2 at row: " << row << " and col: " << j << " with result " << result << std::endl;
                }
            }

            l = range.r + 1;
        }
    }

    return 0;
}