#include <iostream>
 
using namespace std;
 
int main(int argc, char const *argv[]) {
	int T, A, B;
 
	cin >> T; 

	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		cout << A + B << "\n";
	}
	return 0;
}
