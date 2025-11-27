#include<bits/stdc++.h>

using namespace std;

int main()
{
    string lampadas;
    
    while (cin >> lampadas) {
        int n; cin >> n;
        int index[n];
        int x;
        
        for (int i=0; i<n; i++) {
            cin >> x;
            index[i] = x-1;
        }
        for (int i=0; i<n; i++) {
            cout << lampadas[index[i]];
        }
        cout << "\n";
    }
    
    return 0;
}