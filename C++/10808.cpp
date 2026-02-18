#include<iostream>
using namespace std;

int main() 
{
	string S;
	cin >> S;

	int alphabet[26] = {};

	for (int i = 0; i < S.length(); i++)
	{ alphabet[int(S[i])-97]++; }

	for (int num : alphabet)
	{ cout << num << " "; }
}

// 다시 해보기