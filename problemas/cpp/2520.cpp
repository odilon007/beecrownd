#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, m;
    
    while(cin >> n >> m) {
    
        vector<vector<int>> matriz(n, vector<int>(m));
        pair<int, int> pos1;
        pair<int, int> pos2;
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                cin >> matriz[i][j];
                if (matriz[i][j] == 2) {
                    pos2 = {i, j};
                } else if (matriz[i][j] == 1) {
                    pos1 = {i, j};
                }
            }
        }
        
        int distance = abs(pos1.first - pos2.first) + abs(pos1.second - pos2.second);
        cout << distance << endl;
    }
    return 0;
}