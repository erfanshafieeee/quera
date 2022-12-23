#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int t;
    cin >> t;
    int a[t][3];
    int w[t];
    int x[t];
    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> a[i][j];
        }
    }
    for (int i = 0; i < t; i++)
    {
        x[i] = a[i][1] + (a[i][0] - 1) * a[i][2];
        w[i] = floor(x[i] / a[i][0]);
    }
    for (int i = 0; i < t; i++)
    {
        if ((w[i] >= a[i][1]) || (w[i] * a[i][0] < x[i]))
            cout << "-1" << endl;
        else
            cout << w[i] - a[i][2] << endl;
    }

    return 0;
}