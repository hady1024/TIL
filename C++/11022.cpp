#include <iostream>
 
using namespace std;
 
int main(int argc, char const *argv[]) {
 
	int T;
	cin >> T;	
	
	for (int i = 1; i <= T; i++) {
		int a;
		int b;
		cin >> a >> b;
 
		cout << "Case #" << i << ": " << a << " + " << b << " = " << a + b << "\n"; 
	}
	return 0;
}

// 참고한것 다시 해보기