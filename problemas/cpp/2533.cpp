#include<bits/stdc++.h>
using namespace std;

int main()
{
    int m;
    
    while (cin >> m) {
        int x, y;
        int numerador=0;
        int denominador=0;
        
        for (int i=0; i<m; i++) {
            cin >> x >> y;
            numerador += x*y;
            denominador += y*100;
        }
        
        float ira = (float)numerador/denominador;
        
        cout << fixed << setprecision(4);
        cout << ira << endl;
        
    }
    return 0;
}