#include <iostream>
#include <fstream>

enum Play {
    Rock,
    Paper,
    Scrissors
};

Play mapCharToEnum(char inputChar) {
    switch (inputChar) {
        case 'A':
        case 'X':
            return Rock;
        case 'B':
        case 'Y':
            return Paper;
        case 'C':
        case 'Z':
            return Scrissors;
    }
    return Rock;
}

int points(Play play) {
    return play + 1;
}

enum Result {
    Win,
    Draw,
    Lose
};

Result match(Play opponent, Play me) {
    if(opponent == me) {
        return Draw;
    }
    if(opponent == Rock) {
        return me == Paper ? Win : Lose;
    }
    if(opponent == Paper) {
        return me == Scrissors ? Win : Lose;
    }
    return me == Rock ? Win : Lose;
}

int points(Result result) {
    if(result == Win) {
        return 6;
    } else if (result == Draw) {
        return 3;
    } else {
        return 0;
    }
}

Result mapCharToResult(char inputChar) {
    switch (inputChar) {
        case 'X':
            return Lose;
        case 'Y':
            return Draw;
        case 'Z':
            return Win;
    }
    return Win;
}

Play requiredPlayForResult(Play opponent, Result result) {
    if(result == Draw) {
        return opponent;
    }

    if(opponent == Rock){
        return result == Win ? Paper : Scrissors;
    } else if (opponent == Paper) {
        return result == Win ? Scrissors : Rock;
    } else {
        return result == Win ? Rock : Paper;
    }
}


int main() {
    std::ifstream infile("input.txt");

    std::string line;

    int sumPart1 = 0;
    int sumPart2 = 0;

    while (std::getline(infile, line)) {
        Play opponent = mapCharToEnum(line[0]);
        Play me = mapCharToEnum(line[2]);
        Result result = match(opponent, me);
        int pPart1 = points(result) + points(me); 
        sumPart1 += pPart1;

        Result part2 = mapCharToResult(line[2]);
        Play meRequired = requiredPlayForResult(opponent, part2);
        int pPart2 = points(part2) + points(meRequired);
        sumPart2 += pPart2;
    }

    std::cout << "Points Part1: " << sumPart1;
    std::cout << "Points Part: " << sumPart2;

    return 0;
}