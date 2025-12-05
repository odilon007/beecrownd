#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    while (cin >> n) {
        int qtd=0;
        while (n != 0) {
            if (n % 2 == 0) {
                qtd++;
                n /= 2;
            } else break;
        }
        cout << qtd << endl;
    }
    

    return 0;
}