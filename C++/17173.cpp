#include <iostream>

using namespace std;

int main(){
	int n, m;
	int sum = 0;
	cin >> n >> m;
	
	int k[m+1] = {0};
	int b[n+1] = {0};
	
	for(int i=0; i<m; i++){
		cin >> k[i];
	}
	
	for(int i=0; i<m; i++){
		for(int j=1; j<=n; j++){
			if(j%k[i] == 0) b[j] = j;
		}
	}
	
	for(int i=1; i<=n; i++){
		sum += b[i];
	}
	
	cout << sum;
	
	return 0;
}

