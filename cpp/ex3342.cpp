#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, total, b, p;
    
    cin >> n;
    total = n*n;
    p = total/2;
    b = total - p;
    cout << b << " casas brancas e " << p << " casas pretas\n";
    
    return 0;
}
