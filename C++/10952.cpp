#include <stdio.h>


int main() {
	
	int a, b;
	
	while(1) {
		scanf("%d %d", &a, &b);
		
		if(a == 0 && b == 0) break;
		
		printf("%d \n", a + b);
	}

	
	return 0;
}

// 와일문 참고 한것 다시 풀어보기