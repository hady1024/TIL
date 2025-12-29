#include <iostream>
using namespace std;

int main() {
	int num, answer = 0;
	int square = 0;

	for (int i = 0; i < 5; i++) {
		cin >> num;

		square += num * num;
	}
	answer = square % 10;

	cout << answer;
}

// 다시 해보기