#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    while (cin >> t) {

        vector<vector<int>> ops(t);
        int x, y, z;
        char temp;

        for (int i = 0; i < t; i++) {
            cin >> x >> y >> temp >> z;
            ops[i] = {x, y, z};
        }

        vector<string> losers;
        int winers = 0;
        string n;
        int e;
        char op;

        for (int i = 0; i < t; i++) {
            cin >> n >> e >> op;
            e--;
            if (e < 0 || e >= t) {
                losers.push_back(n);
                continue;
            }

            switch (op) {
                case 'I': {
                    bool ok = true;
                    if (ops[e][0] + ops[e][1] == ops[e][2]) ok = false;
                    if (ops[e][0] - ops[e][1] == ops[e][2]) ok = false;
                    if (ops[e][0] * ops[e][1] == ops[e][2]) ok = false;
                    if (ops[e][1] != 0 && ops[e][0] / ops[e][1] == ops[e][2]) ok = false;

                    if (ok) winers++;
                    else losers.push_back(n);
                    break;
                }

                case '+':
                    if (ops[e][0] + ops[e][1] == ops[e][2]) winers++;
                    else losers.push_back(n);
                    break;

                case '-':
                    if (ops[e][0] - ops[e][1] == ops[e][2]) winers++;
                    else losers.push_back(n);
                    break;

                case '*':
                    if (ops[e][0] * ops[e][1] == ops[e][2]) winers++;
                    else losers.push_back(n);
                    break;

                case '/':
                    if (ops[e][1] != 0 && ops[e][0] / ops[e][1] == ops[e][2]) winers++;
                    else losers.push_back(n);
                    break;
            }
        }

        if (winers == t) {
            cout << "You Shall All Pass!\n";
        } else if (winers == 0) {
            cout << "None Shall Pass!\n";
        } else {
            sort(losers.begin(), losers.end());
            for (int i=0; i<losers.size(); i++) {
                if (i > 0) cout << " ";
                cout << losers[i];
            }
            cout << "\n";
        }
    }

    return 0;
}
    
