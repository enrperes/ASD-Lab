#include <iostream>
#include <string>

int main() {
    std::string str;
    std::cout << "Enter a string: ";
    std::getline(std::cin, str);
    for (int i = str.length() - 1; i >= 0; i--) {
        std::cout << str[i];
    }
    std::cout << std::endl; 
    return 0;
}   