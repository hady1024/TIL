#include <iostream>

using namespace std;

int T;

int main() {
    cin >> T;

    while(T--) {
        string s;
        cin >> s;

        int add = s[0] + s[2] - 96; // 96 = '0'
        cout << add << "\n";
    }

}
