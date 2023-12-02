from pathlib import Path
import regex as re

p = Path(__file__).with_name("input.txt")
file = open(p)

flowRates = {}
tunnels = {}
dp = [{}] * 32

for line in file.readlines():
    matches = re.findall("Valve (\w\w).*rate=(\d+); tunnels? leads? to valves? (.*)", line)

    valve = matches[0][0]

    flowRate = int(matches[0][1])
    flowRates[valve] = flowRate

    tunnelsTo = matches[0][2].split(", ")
    tunnels[valve] = tunnelsTo

start = 'AA'
dp[0]['AA'] = (0, 0, []) # flowRate, total, valvesOpen

for i in range(1, 31):
    valves = dp[i-1]
    valvesForCurrentLevel = {}

    for (valve, maxAtPreviousLevel) in valves.items():
        (currentFlowRate, currentTotal, valvesOpen) = maxAtPreviousLevel

        newTotal = currentTotal + currentFlowRate
        
        # Two Decisions: we open valve, or we move somewhere else
        if True:
            targetValve = valve
            if not valve in valvesOpen:
                newFlowRate = currentFlowRate + flowRates[targetValve]
                newValvesOpen = valvesOpen + [targetValve]
            else:
                newFlowRate = currentFlowRate
                newValvesOpen = valvesOpen

            newItem = (newFlowRate, newTotal, newValvesOpen)

            if not targetValve in valvesForCurrentLevel:
                valvesForCurrentLevel[targetValve] = newItem
            elif valvesForCurrentLevel[targetValve] == newFlowRate and valvesForCurrentLevel[targetValve][1] < newTotal:
                valvesForCurrentLevel[targetValve] = newItem
            elif valvesForCurrentLevel[targetValve][0] < newFlowRate:
                valvesForCurrentLevel[targetValve] = newItem


        for targetValve in tunnels[valve]:
            newItem = (currentFlowRate, newTotal, valvesOpen)

            if not targetValve in valvesForCurrentLevel:
                valvesForCurrentLevel[targetValve] = newItem
    
            elif valvesForCurrentLevel[targetValve] == newFlowRate and valvesForCurrentLevel[targetValve][1] < newTotal:
                valvesForCurrentLevel[targetValve] = newItem
            elif valvesForCurrentLevel[targetValve][0] < newFlowRate:
                valvesForCurrentLevel[targetValve] = newItem

                

    dp[i] = valvesForCurrentLevel
    print("Minute", i)
    print(dict(sorted(dp[i].items())))

part1 = max(dp[30].values(), key=lambda p: p[1])[1]
print("Part 1", part1)