#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main()
{
    int C[20];
    srand(unsigned(time(0)));
    for (int i = 0; i < 20; i++)
    {
        C[i] = rand() % 10;
        cout << C[i] << " ";
    };
    cout << endl;
    int Min = 100;
    bool flag = false;
    for (int n = 0; n < 20; n++)
    {
        if ((C[n] > 0) && (C[n] < Min))
        {
            Min = C[n];
            flag = true;
        };
    }
    if (flag)
    {
        cout << Min;
    }
    else
    {
        cout << -1;
    }
    return 0;
}