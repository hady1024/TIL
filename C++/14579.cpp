#include <iostream>
using namespace std;

int main(){
    int A, B;
    cin >> A >> B;

    int sum = 0;

    for(int i=0; i<=A; i++){
        sum += i;
    }

    int tmp = sum;

    for(int i=A+1; i<=B; i++){
        tmp += i;
        sum *= tmp;
        sum %= 14579;
    }

    cout << sum << "\n";

    return 0;
}

