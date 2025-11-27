#include <bits/stdc++.h>

using namespace std;
int main()
{
    int n, q;
    
    while (cin >> n >> q) {
        vector<int>  notas(n);
        
        for (int i=0; i<n; i++) {
            cin >> notas[i];
        }
        int x;
        sort(notas.begin(), notas.end(), greater<int>());
        
        for (int i=0; i<q; i++) {
            cin >> x;
            cout << notas[x-1] << "\n";
        }
        
    }

    return 0;
}