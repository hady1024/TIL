#include <iostream>
using namespace std;

int main() {
	int T;
	int a, b, c;
	char comma;
	
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> a >> comma >> b;
		c = a + b;
		cout << c << endl;
	}
}

// 다시 해보기