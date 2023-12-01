#include <iostream>
#include <fstream>
#include <sstream>
#include <regex>
#include <map>

struct Valve
{
    Valve(int flowIn, std::vector<std::string> connectedValvesIn) : flow(flowIn), connectedValves(connectedValvesIn) {}
    Valve() {}

    int flow;
    std::vector<std::string> connectedValves;
};

void part1(std::map<std::string, Valve> valves) {
    std::vector<std::map<std::string, int>> dp(31);

    dp[0]["AA"] = 0;

    for(int i = 1; i <= 30; i++) {
        for(auto &pair: dp[])
    }

    int max = 0;
    for(auto &pair: dp[30]) {
        max = std::max(max, std::get<1>(pair));
    }
    std::cout << "Part 1: " << max << std::endl; 
}

int main()
{
    std::ifstream infile("input.txt");
    std::string tmp;
    std::regex pattern("Valve (..) has flow rate=(..?); tunnels? leads? to valves? (.*)");

    std::map<std::string, Valve> valves;

    while (std::getline(infile, tmp))
    {
        std::smatch matches;
        std::regex_search(tmp, matches, pattern);

        std::string valveCode = matches[1];

        int flowRate = std::stoi(matches[2]);

        std::stringstream ss(matches[3]);
        std::vector<std::string> connectedValves;
        while (std::getline(ss, tmp, ','))
        {
            connectedValves.push_back(tmp);
        }

        valves[valveCode] = Valve(flowRate, connectedValves);
    }

    part1(valves);

}