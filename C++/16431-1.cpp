#include <iostream>

using namespace std;

int main() {
    int br,bc,dr,dc,lr,lc;
    cin>>br>>bc>>dr>>dc>>lr>>lc;
    int m=min(abs(lr-br),abs(lc-bc));
    int sum=abs(lr-br)+abs(lc-bc)-m;
    int sum1=abs(lr-dr)+abs(lc-dc);

    if(sum>sum1) cout<<"daisy";

    else if(sum<sum1) cout<<"bessie";
    else cout<<"tie";
}

