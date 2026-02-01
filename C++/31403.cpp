#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string A, B, C;

    cin >> A >> B >> C;

    cout << stoi(A) + stoi(B) - stoi(C) << '\n';
    cout << stoi(A + B) - stoi(C) << '\n';

    return 0;
}

// 다시 해보기(오늘도 잘 안됐음 02/01)