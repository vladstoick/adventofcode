#include <iostream>
#include <fstream>
#include <sstream>
#include <string_view>
#include <ranges>

enum Type
{
    Wall = '#',
    Empty = '.',
    Sand = 'o'
};

using matrix = std::vector<std::vector<Type>>;
const int N = 200;
const int M = 1000;

const int N_START = 0;
const int N_END = 171;
const int COL_START = 0;
const int COL_END = 1000;
void printDebug(matrix m)
{
    for (int i = N_START; i < N_END; i++)
    {
        for (int j = COL_START; j <= COL_END; j++)
        {
            if (m[i][j] == Wall)
            {
                std::cout << "#";
            }
            else if (m[i][j] == Sand)
            {
                std::cout << "o";
            }
            else
            {
                std::cout << ".";
            }
        }
        std::cout << std::endl;
    }
}

const int DROP_I = 0;
const int DROP_J = 500;

bool process(matrix &m)
{
    int i = DROP_I;
    int j = DROP_J;

    while (true)
    {
        if (i + 1 == N)
        {
            return false;
        }

        if (m[i + 1][j] == Empty)
        {
            i = i + 1;
        }
        else if (m[i + 1][j - 1] == Empty)
        {
            i = i + 1;
            j = j - 1;
        }
        else if (m[i + 1][j + 1] == Empty)
        {
            i = i + 1;
            j = j + 1;
        }
        else
        {
            m[i][j] = Sand;
            return true;
        }
    }

    return false;
}

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    auto mPart1 = matrix(N, std::vector<Type>(M, Empty));
    auto mPart2 = matrix(N, std::vector<Type>(M, Empty));

    int maxI = 0;

    while (std::getline(infile, line))
    {

        std::stringstream ss(line);
        std::string temp;
        std::vector<std::tuple<int, int>> row;

        while (std::getline(ss, temp, ','))
        {
            int l = std::stoi(temp);
            std::getline(ss, temp, ' ');
            int r = std::stoi(temp);
            std::getline(ss, temp, ' ');

            row.push_back(std::make_tuple(r, l));
            maxI = std::max(maxI, r);
        }

        for (int k = 0; k < row.size() - 1; k++)
        {
            auto [leftI, leftJ] = row[k];
            auto [rightI, rightJ] = row[k + 1];

            for (int i = std::min(leftI, rightI); i <= std::max(leftI, rightI); i++)
            {
                for (int j = std::min(leftJ, rightJ); j <= std::max(leftJ, rightJ); j++)
                {
                    mPart1[i][j] = Wall;
                    mPart2[i][j] = Wall;
                }
            }
        }
    }

    for (int step = 1; step <= 10000; step++)
    {
        bool result = process(mPart1);

        if (!result)
        {
            std::cout << "Part 1: " << step - 1 << std::endl;
            break;
        }
    }

    for (int i = 0; i < M; i++)
    {
        mPart2[maxI + 2][i] = Wall;
    }

    for (int step = 1; step <= 1000000; step++)
    {
        process(mPart2);

        if (mPart2[DROP_I][DROP_J] == Sand)
        {
            std::cout << "Part 2: " << step  << std::endl;
            break;
        }
    }
    return 0;
}