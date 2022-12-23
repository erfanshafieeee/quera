#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int a[n];
    string s[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++)
    {
        if (a[i] <= 1023)
        {
            s[i] = "B";
        }
        else if (a[i] >= 1024 && a[i] <= 1048575)
        {
            a[i] = a[i] / 1024;
            s[i] = "KiB";
        }
        else if (a[i] >= 1048576)
        {
            a[i] = a[i] / 1048576;
            s[i] = "MiB";
        }
    }
    for (int i = 0; i < n; i++)
    {

        cout << a[i] << s[i] << endl;
    }

    return 0;
}