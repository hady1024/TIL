#include <iostream>
 
using namespace std;
 
int main(int argc, char const *argv[]) {
    int A, B;
 
    cin >> A >> B;
 
    cout << A * (B % 10) << "\n";
    cout << A * ((B % 100) / 10) << "\n";
    cout << A * (B / 100) << "\n";
    cout << A * B;
 
    return 0;
}
