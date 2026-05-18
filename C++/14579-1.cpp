#include <iostream>
using namespace std;

int main()
{
	int a, b, result = 1, sum = 0;
	cin >> a >> b;
	for (int i = a; i <= b; i++) {
		for (int j = 1; j <= i; j++) sum += j;
		result = (result * sum) % 14579;
		sum = 0;
	}
	cout << result;

	return 0;
}

// 다시 해보기