#include <iostream>
#include <fstream>
#include <string>

class File
{
public:
    File(std::string nameIn, int sizeIn) : name(nameIn), size(sizeIn) {}

    int size;
    std::string name;
};

class Folder
{
public:
    Folder(std::string nameIn) : name(nameIn) {}
    Folder(std::string nameIn, Folder *parentIn) : name(nameIn), parent(parentIn) {}

    void addChild(std::string nameIn)
    {
        if (getChild(name) == nullptr)
        {
            Folder newFolder = Folder(nameIn, this);
            children.push_back(newFolder);
        }
    }

    Folder *getChild(std::string name)
    {
        for (int i = 0; i < children.size(); i++)
        {
            if (children[i].name == name)
            {
                return &children[i];
            }
        }

        return nullptr;
    }

    void addFile(std::string nameIn, int size)
    {
        files.push_back(File(nameIn, size));
    }

    void measure()
    {
        for (int i = 0; i < files.size(); i++)
        {
            size += files[i].size;
        }
        for (int i = 0; i < children.size(); i++)
        {
            children[i].measure();
            size += children[i].size;
        }
    }

    int part1()
    {
        int result = 0;
        if (size <= 100000)
        {
            result += size;
        }
        for (int i = 0; i < children.size(); i++)
        {
            result += children[i].part1();
        }
        return result;
    }

    int minFolderToRemove(int requiredRemoval)
    {
        int min = 70000000;
        for (int i = 0; i < children.size(); i++)
        {
            int res = children[i].minFolderToRemove(requiredRemoval);
            if (res < min)
            {
                min = res;
            }
        }

        if (min != 70000000)
        {
            return min;
        }

        if (size >= requiredRemoval)
        {
            std::cout << "can remove " << name << " for size " << size << std::endl;
            return size;
        }

        return 70000000;

        // return size >= requiredRemoval ? size : -1;
    }

    int size = 0;
    std::vector<File> files;
    std::vector<Folder> children;
    Folder *parent;
    std::string name;
};

int main()
{
    std::ifstream infile("input.txt");
    std::string line;

    Folder root = Folder("/");
    Folder *current = &root;

    while (std::getline(infile, line))
    {
        std::cout << "Currently in " << current->name << std::endl;
        if (line[0] == '$')
        {
            if (line.substr(2, 2) == "cd")
            {
                std::string target = line.substr(5);

                std::cout << "Cd-ing to " << target << std::endl;

                if (target == "/")
                {
                    current = &root;
                }
                else if (target == "..")
                {
                    if (current->parent != nullptr)
                    {
                        current = current->parent;
                    }
                }
                else
                {
                    current = current->getChild(target);
                }
            }
        }
        else
        {
            if (line.substr(0, 3) == "dir")
            {
                std::string folder = line.substr(4);
                current->addChild(folder);
            }
            else
            {
                int space = line.find(" ");
                int size = std::stoi(line.substr(0, space));
                std::string name = line.substr(space);

                current->addFile(name, size);
            }
        }
    }

    root.measure();
    // int part1;
    std::cout << "Root size " << root.size << std::endl;
    std::cout << "Part 1 " << root.part1() << std::endl;
    std::cout << "Part 2 " << root.minFolderToRemove(30000000 - (70000000 - root.size));

    return 0;
}