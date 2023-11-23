#include <fstream>
#include <vector>
#include <tuple>
#include <iostream>

const int N = 1000;
const int S = 500;

// const int N = 6;
// const int S = 0;

// const int RL = 10;

using matrix = std::vector<std::vector<bool>>;
struct pos
{
    int i, j;
    pos(int iIn, int jIn) : i(iIn), j(jIn){};
};

using rope = std::vector<pos>;

matrix generate(int n)
{
    return matrix(n, std::vector<bool>(n, false));
}

void printDebug(matrix v, rope r)
{
    std::cout << "----" << std::endl;
    int i = 0;
    for (auto rowIt = v.rbegin(); rowIt != v.rend(); rowIt++)
    {
        auto row = *rowIt;
        std::cout << i << ":";
        int j = 0;
        for (auto columnIt = row.begin(); columnIt != row.end(); columnIt++)
        {
            auto v = *columnIt;
            auto actualI = N - i - 1;

            if (actualI == r[0].i && j == r[0].j)
            {
                std::cout << "H";
            }

            else
            {
                bool didMatch = false;
                for (int k = 1; k < r.size(); k++)
                {
                    if (actualI == r[k].i && j == r[k].j)
                    {
                        std::cout << k;
                        didMatch = true;
                        break;
                    }
                }

                if (!didMatch)
                {
                    std::cout << (v ? '#' : '.');
                }
            }

            j++;
        }
        i++;
        std::cout << std::endl;
    }
}

pos applyCommand(pos p, char command)
{
    int di = 0;
    int dj = 0;
    switch (command)
    {
    case 'R':
        dj = 1;
        break;
    case 'L':
        dj = -1;
        break;
    case 'U':
        di = 1;
        break;
    case 'D':
        di = -1;
        break;
    }
    return pos(p.i + di, p.j + dj);
}

bool isOk(pos first, pos second)
{
    int rowDistance = std::abs(first.i - second.i);
    int colDistance = std::abs(first.j - second.j);

    return rowDistance <= 1 && colDistance <= 1;
}

pos moveSecondBasedOnFirst(pos first, pos second)
{   
    int rowDistance = std::abs(first.i - second.i);
    int colDistance = std::abs(first.j - second.j);

    int rowDirection = first.i > second.i ? 1 : -1;
    int colDirection = first.j > second.j ? 1 : -1;

    // If they are directly two across
    if(rowDistance == 2 && colDistance == 0) {
        return pos(second.i + (first.i - second.i) / 2, second.j);
    } else if(rowDistance == 0 && colDistance == 2) {
        return pos(second.i, second.j + (first.j - second.j) / 2);
    } else {
        return pos(second.i + rowDirection, second.j + colDirection);
    }

    return second;
}

rope operate(matrix v, rope r, char command)
{
    r[0] = applyCommand(r[0], command);

    for (int i = 1; i < r.size(); i++)
    {
        if (!isOk(r[i - 1], r[i]))
        {
            r[i] = moveSecondBasedOnFirst(r[i - 1], r[i]);
        }
    }

    return r;
}

int solve(int ropeLength) {
std::ifstream infile("input.txt");
    std::string line;

    matrix visited = generate(N);
    rope r = rope(ropeLength, pos(S, S));

    visited[r[0].i][r[0].j] = true;

    while (std::getline(infile, line))
    {
        char command = line[0];
        int count = std::stoi(line.substr(line.find(" ") + 1));
        while (count--)
        {
            r = operate(visited, r, command);
            visited[r[r.size() - 1].i][r[r.size() - 1].j] = true;
        }
    }

    int part1 = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            part1 += visited[i][j] ? 1 : 0;
        }
    }

    return part1;
}

int main()
{
    std::cout << "Part 1: " << solve(2) << std::endl;
    std::cout << "Part 2: " << solve(10) << std::endl;

    return 0;
}