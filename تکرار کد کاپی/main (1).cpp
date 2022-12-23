#include <iostream>
using namespace std;
int main()
{
    int x, w;
    string s = "codecup6";
    cin >> x;
    while (x > 8)
    {
        x = x - 8;
    }
    cout << s[x - 1];

    return 0;
}