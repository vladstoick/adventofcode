#include <iostream>
#include <fstream>
#include <queue>

using matrix = std::vector<std::vector<int>>;
struct pos
{
    int i;
    int j;
    pos(int iIn, int jIn)
    {
        i = iIn;
        j = jIn;
    }
};

bool operator==(const pos &lhs, const pos &rhs)
{
    return lhs.i == rhs.i && lhs.j == rhs.j;
}

int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};

int part1(matrix heights, pos start, pos end)
{
    int n = heights.size();
    int m = heights[0].size();

    matrix distance = matrix(n, std::vector<int>(m, 10000));
    distance[start.i][start.j] = 0;
    std::queue<pos> q;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if(heights[i][j] == 0) {
                q.push(pos(i,j));
                distance[i][j] = 0;
            }
        }
    }

    

    while (!q.empty())
    {
        auto current = q.front();
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            pos newPos = pos(current.i + di[i], current.j + dj[i]);
            if (newPos.i < 0 || newPos.i >= n)
                continue;
            if (newPos.j < 0 || newPos.j >= m)
                continue;
            if (heights[newPos.i][newPos.j] - heights[current.i][current.j] > 1)
                continue;
            if (distance[newPos.i][newPos.j] > distance[current.i][current.j] + 1)
            {
                distance[newPos.i][newPos.j] = distance[current.i][current.j] + 1;
                if (newPos != end)
                {
                    q.push(newPos);
                }
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            std::cout << (distance[i][j] == 10000 ? "." : std::to_string(distance[i][j])) << "\t";
        }
        std::cout << std::endl;
    }

    return distance[end.i][end.j];
}

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    // matrix m = matrix(std::vector<)
    matrix m;
    pos start = pos(0, 0);
    pos end = pos(0, 0);
    while (std::getline(infile, line))
    {
        std::vector<int> row;
        for (int i = 0; i < line.size(); i++)
        {
            char c = line[i];
            if (line[i] == 'S')
            {
                start = pos(m.size(), i);
                c = 'a';
            }
            else if (line[i] == 'E')
            {
                end = pos(m.size(), i);
                c = 'z';
            }

            row.push_back(c- 'a');
        }
        m.push_back(row);
    }

    int p1 = part1(m, start, end);

    std::cout << "Part 1: " << p1 << std::endl;

    return 0;
}