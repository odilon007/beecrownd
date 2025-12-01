#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    while (cin >> n) {
        int m, l; cin >> m >> l;

        int cartasm[m][n];
        int cartasl[l][n];

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                cin >> cartasm[i][j];
            }
        }
        for (int i=0; i<l; i++) {
            for (int j=0; j<n; j++) {
                cin >> cartasl[i][j];
            }
        }
        int cm, cl; cin >> cm >> cl;
        cm--; cl--;
        
        int a; cin >> a;
        a--;

        if (cartasm[cm][a] > cartasl[cl][a]) {
            cout << "Marcos\n";
        } else if (cartasm[cm][a] < cartasl[cl][a]) {
            cout << "Leonardo\n";
        } else {
            cout << "Empate\n";
        }

    }

    return 0;
}
