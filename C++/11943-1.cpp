#include <iostream>
using namespace std;
int main(void){
    int a, b, c, d;
    cin>>a>>b>>c>>d;
    if (a + d <= b + c)
        cout<<a + d;
    else
        cout<<b + c;
    return 0;
}

// 다시 해보기