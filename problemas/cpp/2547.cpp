#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, amin, amax;
    while (cin >> n >> amin >> amax) {
        int ai, qtd=0;
        for (int i=0; i<n; i++) {
            cin >> ai;
            if (ai >= amin && ai <= amax) {
                qtd++;
            }
        }
        cout << qtd << endl;
    }
    return 0;
}