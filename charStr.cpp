#include <iostream>
using namespace std;

#include <string>

int StringHash( const string& str, int modulus)
{
        const int kMult = 997;
        int val         = 0;

        for (char c : str) {
                std::cout << c << std::endl;
                std::cout << (val * kMult + c)  << std::endl;

                val = ( val * kMult + c ) % modulus;
        }

        return val;
}

int main()
{
        string s = "anish";
        double c = StringHash(s, 5);

        std::cout << "------------------------------" << c << std::endl;
}
