#include <iostream>
using namespace std;

int main() {
	int a, b;
	int result[4] = {};
	cin >> a >> b;

	result[0] = a * (b % 10);
	result[1] = a * (b % 100 / 10);
	result[2] = a * (b / 100);
	result[3] = a * b;

	cout << result[0] << endl << result[1] << endl << result[2] << endl << result[3] << endl;
}


// 참고한것 다시 해보기