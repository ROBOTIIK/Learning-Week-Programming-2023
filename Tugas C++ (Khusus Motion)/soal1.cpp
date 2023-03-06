#include <iostream>
#include <iomanip>

int tukar(int &a, int &b){
    int temp = a;
    return a = b, b = temp;
}

char tukar(char &a, char &b){
    char temp = a;
    return a = b, b = temp;
}

double tukar(double &a, double &b){
    double temp = a;
    return a = b, b = temp;
}

bool tukar(bool &a, bool &b){
    bool temp = a;
    return a = b, b = temp;
}

std::string tukar(std::string &a, std::string &b){
    std::string temp = a;
    return a = b, b = temp;
}

int main(){
    int n;
    char a;
    int i1, i2;
    char c1, c2;
    double d1, d2;
    bool b1, b2;
    std::string s1, s2;

    std::cin >> n;

    if(n >= 1 && n <= 10){
        for(int x = 0; x < n; x++){
            std::cin >> a;

            switch (a)
            {
            case 'i':
                std::cin >> i1 >> i2;
                tukar(i1, i2);
                std::cout << i1 << " " << i2 << "\n";
                break;
            case 'c':
                std::cin >> c1 >> c2;
                tukar(c1, c2);
                std::cout << c1 << " " << c2 << "\n";
                break;
            case 'd':
                std::cin >> d1 >> d2;
                tukar(d1, d2);
                std::cout << std::fixed << std::setprecision(1) << d1 
                        << " " 
                        << std::fixed << std::setprecision(1) << d2 
                        << "\n";
                break;
            case 'b':
                std::cin >> b1 >> b2;
                tukar(b1, b2);
                std::cout << b1 << " " << b2 << "\n";
                break;
            case 's':
                std::cin >> s1 >> s2;
                tukar(s1, s2);
                std::cout << s1 << " " << s2 << "\n";
                break;
            
            default:
                break;
            }
        }
    } else{
        std::cout << "Number of input is out of scope!";
    }
}
