#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int main(int argc, char *argv[])
{
	int bx, by;
	int dx, dy;
	int jx, jy;
	int countB;
	int countD;
	cin >> bx >> by;
	cin >> dx >> dy;
	cin >> jx >> jy;

	countB = max(abs(jx - bx), abs(jy - by));
	countD = abs(jx - dx) + abs(jy - dy);

	if (countB < countD) {
		cout << "bessie" << endl;
	}
	else if (countB > countD) {
		cout << "daisy" << endl;
	}
	else {
		cout << "tie" << endl;
	}

	return 0;
}

// 파이썬때 생각하면서 했는데 얼추 되다가 단추가 다 안꿰어져서 참고함 다시해보기