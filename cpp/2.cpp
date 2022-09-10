#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    int dummy = n;
    int count = 0;
    cin >> n;
    int arr[n + 1];

    for (int i = 1; i <= n; i++)
    {
        cin >> arr[i];
    }

    for (int i = 1; i <= n; i++)
    {
        if (arr[i] < 0)
        {
            count += 1;
        }
    }

    dummy = n - count;

    if (dummy % 2 == 0)
    {
        cout << arr[dummy - 1];
    }
    else
    {
        cout << arr[dummy];
    }

    return 0;
}