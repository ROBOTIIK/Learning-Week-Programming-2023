#include <string>

class optimus
{
private:
    int x;
    int y;
    int xe;
    int ye;
    int loop;
    std::string arah[10]; //batasan perintah
public:
    optimus();
    void console();
    void track(int index, int a, int b);
    void compute(int c, int d);
    void printer();
};

