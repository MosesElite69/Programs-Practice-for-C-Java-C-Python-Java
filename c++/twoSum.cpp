#include <iostream>
using namespace std;

int addTwoNumbers(int A, int B)
{
    return A + B;
}

int main()
{
    int A = 4, B = 11;

    cout << "sum = " << addTwoNumbers(A, B);
    return 0;
}