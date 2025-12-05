#include<bits/stdc++.h>
using namespace std;


int contarVizinhos(const vector<vector<int>>& matriz, int i, int j) {
    vector<pair<int,int>> pos={
        {-1,0}, {0,-1}, {0,1}, {1,0}
    };
    int vizinhos=0, a, b;
    for (auto p : pos) {
        a = i + p.first;
        b = j + p.second;
        if (a >= 0 && a < matriz.size() && b >= 0 && b < matriz[0].size()) {
            if (matriz[a][b] == 9) {
                vizinhos++;
            }
        }
    }
    return vizinhos;
}

int main()
{
    int n, m;
    
    while (cin >> n >> m) {
        vector<vector<int>> matriz(n, vector<int>(m));
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                int x;
                cin >> x;
                if (x == 1) {
                    matriz[i][j] = 9;
                }
                else {
                    matriz[i][j] = x;
                }
            }
        }
        vector<vector<int>> novaMatriz(n, vector<int>(m));
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (matriz[i][j] == 9) {
                    novaMatriz[i][j] = 9;
                } else {
                    int viz;
                    viz = contarVizinhos(matriz, i, j);
                    novaMatriz[i][j] = viz;
                }
            }
        } 
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                cout << novaMatriz[i][j];
            } cout << "\n";
        }    
    }
    return 0;
}