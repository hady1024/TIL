#include <iostream>

using namespace std;


int main() {

	int a;
	bool cnt[42] = { false, };

	int res = 0;

	for (int i = 0; i < 10; i++) {
		cin >> a;
		
		cnt[a % 42] = true;
	}

	for (int i = 0; i < 42; i++) {
		if (cnt[i]) res++;
	}

	cout << res;
	

	return 0;
}

// 다시 해보기