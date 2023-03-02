#include <iostream>
#include <string> // need this to access std::string

/*Declaring functions to swap values between two variables
  accepted datatypes = int, char, double, bool, std::string*/ 

void tukar(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
    std::cout << "  " << a << " " << b << std::endl << std::endl;
}

void tukar(char &a, char &b) {
    char tmp = a;
    a = b;
    b = tmp;
    std::cout << "  " << a << " " << b << std::endl << std::endl;
}

void tukar(double &a, double &b) {
    double tmp = a;
    a = b;
    b = tmp;
    std::cout << "  " << a << " " << b << std::endl << std::endl;
}

void tukar(bool &a, bool &b) {
    bool tmp = a;
    a = b;
    b = tmp;
    std::cout << "  " << a << " " << b << std::endl << std::endl;
}

void tukar(std::string &a, std::string &b) {
    std::string tmp = a;
    a = b;
    b = tmp;
    std::cout << "  " << a << " " << b << std::endl << std::endl;
}

int main() {
    
    // Query user for number of inputs
    int n;
    std::cin >> n;

    char type;
    std::string k, j;
    for (int i = 0; i < n; i++) {
        // Query user for input's datatype
        std::cin >> type;
        switch (type)
        {
        case 'i': // int handler
            int a; std::cin >> a;
            int b; std::cin >> b;
            tukar(a, b);
            continue;
        case 'c': // char handler
            char c; std::cin >> c;
            char d; std::cin >> d;
            tukar(c, d);
            continue;
        case 'd': // double handler
            double e; std::cin >> e;
            double f; std::cin >> f;
            tukar(e, f);
            continue;
        case 'b': // bool handler
            bool g; std::cin >> g;
            bool h; std::cin >> h;
            tukar(g, h);
            continue;
        case 's': // std::string handler
            std::cin >> j;
            std::cin >> k;
            tukar(j, k);
            continue;
        default:
            continue;
        }
    }

    return 0;
}