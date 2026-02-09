#include <iostream>

using namespace std;


int main() {

	double jumsu[1001];
	int t, max = -1;
	double sum = 0;

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> jumsu[i];
		if (max < jumsu[i]) max = jumsu[i];
	}

	for (int i = 0; i < t; i++) {
		jumsu[i] = jumsu[i] / max * 100;
		sum += jumsu[i];
	}

	cout << sum / t;
	
	

	return 0;
}

