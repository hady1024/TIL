#include <iostream>

using namespace std;

int main() {

    ios::sync_with_stdio(false); 
    cin.tie(NULL); 

    int t;
    int a, b;

    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> a >> b;
        cout << a + b << '\n';
    }

    return 0;
}

// 다시 해보기
