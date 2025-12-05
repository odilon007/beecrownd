#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    int t, d;
    
    while (cin >> n) {
        vector<int> dias;
        float vel=-11111;
        
        for (int i=0; i<n; i++) {
            float temp;
            cin >> t >> d;
            temp = (float)d/t;
            
            if (temp > vel){
                dias.push_back(i+1);
                vel = temp;
            }
        }
        for (auto dia : dias) {
            cout << dia << endl;
        }
    }
    return 0;
}