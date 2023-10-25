#include <iostream>

int main() {
    std::string str;
    std::cout << "Enter a string: ";
    std::getline(std::cin, str);
    int i = str.length() - 1;
    while (i>= 0){
        std::cout << str[i];
        i--;
    }
    std::cout << std::endl;
    return 0;
}   