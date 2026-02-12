#include <iostream>
using namespace std;

int main() {
	char c;
	while (cin >> c) {
		if (65 <= c && c <= 90) cout << char(c + 32);
		else cout << char(c - 32);
	}
}

// 다시 해보기(참고한것)