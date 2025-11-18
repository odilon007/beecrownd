#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n, resposta;
    
    while(cin >> n) {
        for(int i=1; i<=n; i++) {
            cin >> resposta;
            cout << "resposta " << i << ": " << resposta << endl;
        }
    }
    
    return 0;
}