#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, I;
    int qtdcs=0, id, tipo;

    while(cin >> n >> I) {
        for (int i=0; i<n; i++) {
            cin >> id >> tipo;
            if (id == I && tipo == 0) {
                qtdcs++;
            }
        }
        cout << qtdcs << endl;
        qtdcs = 0;
    }

    return 0;
}
