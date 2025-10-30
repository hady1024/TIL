#include <iostream>
 
using namespace std;
 
int main(int argc, char const *argv[]) {
	int N;
	cin >> N;
 
	for (int i = 1; i < 10; i++) {
		cout << N << " * " << i << " = " << N * i << "\n";
	}
	return 0;
}

