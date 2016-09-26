// palindrome
#import <iostream>
#import <unordered_map>

using namespace std;
// first prepare frequncy map

bool CanFormPalindrome(const string& s)
{
        unordered_map<char, int> char_frequencies;

        for ( char c : s) {

                ++char_frequencies[c];
        }


        // now traverse map and look for count ==1 in case of len = even

        for (const auto& p : char_frequencies)
        {
                if (p.second%2==0)
                        return false;
        }

        return true;
}


int main()
{
        std::string s  = "aapmmpaa";
        if (CanFormPalindrome(s))
                std::cout << "Yes !";
        else
                std::cout << "No !";

        return 0;
}
