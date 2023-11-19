#include <fstream>
#include <iostream>
#include <vector>

using matrix = std::vector<std::vector<int>>;

matrix heights;
std::vector<std::vector<bool>> visible;

matrix genertate(int n)
{
    return matrix(n, std::vector<int>(n));
}

void printDebug(matrix v)
{
    std::cout << "----" << std::endl;
    for (auto rowIt = v.begin(); rowIt != v.end(); rowIt++)
    {
        auto row = *rowIt;
        for (auto columnIt = row.begin(); columnIt != row.end(); columnIt++)
        {
            auto v = *columnIt;
            std::cout << v << "\t";
        }
        std::cout << std::endl;
    }
}

template <typename Iterator>
std::vector<int> process(Iterator start, Iterator end)
{
    std::vector<int> presence(10);
    std::vector<int> beauty;

    int i = 0;
    for (auto it = start; it != end; it++)
    {
        auto value = *it;
        int lastPresence = 0;
        for (int j = value; j <= 9; j++)
        {
            lastPresence = std::max(lastPresence, presence[j]);
        }
        presence[value] = i;
        beauty.push_back(i - lastPresence);
        i++;
    }

    return beauty;
}

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    while (std::getline(infile, line))
    {
        std::vector<int> row(line.size());
        std::vector<bool> vrow(line.size());

        for (int i = 0; i < line.size(); i++)
        {
            row[i] = (line[i] - '0');
            vrow[i] = false;
        }

        heights.push_back(row);
        visible.push_back(vrow);
    }

    int n = heights.size();
    int m = heights[0].size();

    std::cout << "Processed matrix with " << n << " lines and " << m << " columns" << std::endl;

    for (int i = 0; i < n; i++)
    {
        int max = -1;
        for (int j = 0; j < m; j++)
        {
            if (heights[i][j] > max)
            {
                max = heights[i][j];
                visible[i][j] = true;
            }
        }

        max = -1;
        for (int j = m - 1; j >= 0; j--)
        {
            if (heights[i][j] > max)
            {
                max = heights[i][j];
                visible[i][j] = true;
            }
        }
    }

    for (int j = 0; j < m; j++)
    {
        int max = -1;
        for (int i = 0; i < n; i++)
        {
            if (heights[i][j] > max)
            {
                max = heights[i][j];
                visible[i][j] = true;
            }
        }

        max = -1;
        for (int i = n - 1; i >= 0; i--)
        {
            if (heights[i][j] > max)
            {
                max = heights[i][j];
                visible[i][j] = true;
            }
        }
    }

    int part1 = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            std::cout << (visible[i][j] ? '1' : '0');
            part1 += visible[i][j] ? 1 : 0;
        }
        std::cout << std::endl;
    }

    std::cout << "Part 1:" << part1 << std::endl;
    std::cout << std::endl;

    // R->L
    matrix rl = genertate(n);

    for (int i = 0; i < n; i++)
    {
        std::vector<int> beautyForRow = process(heights[i].begin(), heights[i].end());
        for (int j = 0; j < m; j++)
        {
            rl[i][j] = beautyForRow[j];
        }
        std::cout << std::endl;
    }

    printDebug(rl);

    // L->R
    matrix lr = genertate(n);
    for (int i = 0; i < n; i++)
    {
        std::vector<int> beautyForRow = process(heights[i].rbegin(), heights[i].rend());
        std::reverse(beautyForRow.begin(), beautyForRow.end());
        for (int j = 0; j < m; j++)
        {
            lr[i][j] = beautyForRow[j];
        }
    }
    printDebug(lr);

    // D->U
    matrix du = genertate(n);
    for (int j = 0; j < m; j++)
    {
        std::vector<int> column;
        for (int i = 0; i < n; i++)
        {
            column.push_back(heights[i][j]);
        }

        std::vector<int> beautyForRow = process(column.begin(), column.end());
        for (int i = 0; i < n; i++)
        {
            du[i][j] = beautyForRow[i];
        }
    }
    printDebug(du);

    // U->D
    matrix ud = genertate(n);
    for (int j = 0; j < m; j++)
    {
        std::vector<int> column;
        for (int i = 0; i < n; i++)
        {
            column.push_back(heights[i][j]);
        }

        std::vector<int> beautyForRow = process(column.rbegin(), column.rend());
        std::reverse(beautyForRow.begin(), beautyForRow.end());
        for (int i = 0; i < n; i++)
        {
            ud[i][j] = beautyForRow[i];
        }
    }
    printDebug(ud);

    matrix beauty = genertate(n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            beauty[i][j] = lr[i][j] * rl[i][j] * ud[i][j] * du[i][j];
        }
    }
    printDebug(beauty);

    int part2 = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            part2 = std::max(part2, beauty[i][j]);
        }
        std::cout << std::endl;
    }

    std::cout << "Part2: " << part2 << std::endl;

    return 0;
}