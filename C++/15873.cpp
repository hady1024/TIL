#include <iostream>
using namespace std;

int main()
{
    int N = 0, sum = 0;
    cin >> N;
    
    if((N % 10) != 0){
        sum += (N % 10);
        N /= 10;

    }
    else{
        sum += 10;
        N /= 100;
    }

    sum += N;
    
    cout << sum << '\n';
    
    return 0;
}


