#include <iostream>
#include <fstream>
#include <queue>

int main()
{
    std::ifstream infile("input.txt");

    std::string line;
    long count = 0;
    std::priority_queue<long, std::vector<long>, std::greater<long> > minq;

    while (std::getline(infile, line))
    {
        if (line.size() == 0)
        {
            std::cout << "Count" << count << "\n";
            minq.push(count);
            if(minq.size() > 3) {
                minq.pop();
            }
            count = 0;
        } else {
            count += std::stoi(line);
        }
    }
    
    std::cout << "Count" << count << "\n";

    minq.push(count);
    if(minq.size() > 3) {
        minq.pop();
    }

    long sum = 0;
    sum += minq.top();
    std::cout << "Result 3rd biggest" << minq.top();
    minq.pop();
    sum += minq.top();
    std::cout << "Result 2nd biggest" << minq.top();
    minq.pop();
    sum += minq.top();
    std::cout << "Result biggest" << minq.top();
    
    std::cout << "Sum" << sum;

    return 0;
}
