#include <bits/stdc++.h>

using namespace std;

int main()
{
    int c; cin >> c;
    vector<string> musicas = {
        "PROXYCITY", "P.Y.N.G.", "DNSUEY!",
        "SERVERS", "HOST!", "CRIPTONIZE",
        "OFFLINE DAY", "SALT", "ANSWER!",
        "RAR?", "WIFI ANTENNAS"
    };
    for (int i=0; i<c; i++) {
        int x, y, music; cin >> x >> y;
        music = x+y;
        cout << musicas[music] << endl;
    }
    return 0;
}