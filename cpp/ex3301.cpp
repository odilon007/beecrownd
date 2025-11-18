#include <iostream>
using namespace std;

int main() {
    int h, z, l;

    while (cin >> h >> z >> l) {
        if ((h > z && h < l) || (h > l && h < z)) {
            cout << "huguinho\n";
        } else if ((z > l && z < h) || (z > h && z < l)) {
            cout << "zezinho\n";
        } else {
            cout << "luisinho\n";
        }
    }

    return 0;
}
