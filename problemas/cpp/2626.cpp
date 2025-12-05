#include <bits/stdc++.h>

using namespace std;

int main()
{
    string d, l, p;
    
    
    while (cin >>d >> l >> p) {
        int mensagem=0;
        if (d == l && d == p){
            mensagem = 0;
            
        } else if (d == l) {
            if (d == "pedra"){
                if (p == "papel") {
                    mensagem = 3;
                } else if (p == "tesoura") {
                    mensagem = 0;
                }
            } else if (d == "papel") {
                if (p == "tesoura") {
                    mensagem = 3;
                } else if (p == "pedra") {
                    mensagem = 0;
                }
            } else {
                if (p == "pedra") {
                    mensagem = 3;
                } else if (p == "papel") {
                    mensagem = 0;
                }
            }
            
        } else if (d == p) {
            if (d == "pedra"){
                if (l == "papel") {
                    mensagem = 2;
                } else if (l == "tesoura") {
                    mensagem = 0;
                }
            } else if (d == "papel") {
                if (l == "tesoura") {
                    mensagem = 2;
                } else if (l == "pedra") {
                    mensagem = 0;
                }
            } else {
                if (l == "pedra") {
                    mensagem = 2;
                } else if (l == "papel") {
                    mensagem = 0;
                }
            }
            
        } else if (p == l) {
            if (p == "pedra"){
                if (d == "papel") {
                    mensagem = 1;
                } else if (d == "tesoura") {
                    mensagem = 0;
                }
            } else if (p == "papel") {
                if (d == "tesoura") {
                    mensagem = 1;
                } else if (d == "pedra") {
                    mensagem = 0;
                }
            } else {
                if (d == "pedra") {
                    mensagem = 1;
                } else if (d == "papel") {
                    mensagem = 0;
                }
            }
        }
        
        
        switch (mensagem) {
            case 0:
                cout << "Putz vei, o Leo ta demorando muito pra jogar...\n";
                break;
            case 1:
                cout << "Os atributos dos monstros vao ser inteligencia, sabedoria...\n";
                break;
            case 2:
                cout << "Iron Maiden's gonna get you, no matter how far!\n";
                break;
            case 3:
                cout << "Urano perdeu algo muito precioso...\n";
                break;
        }
    }
    return 0;
}