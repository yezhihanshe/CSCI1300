
// Author: CS1300 Fall 2017         Hanye Han
// Recitation:    101 - Richard Tillquist
//
// recitation 4

#include <iostream>
using namespace std;
int addNumber(int a, int b)
{
    int x;
    x = a + b;
    return x;
}
void swapTwoNumbers()
{
    int a = 5, b = 10, temp;
    cout << "Before swapping." << endl;
    cout << "a = " << a << ", b = " << b << endl;

    temp = a;
    a = b;
    b = temp;

    cout << "\nAfter swapping." << endl;
    cout << "a = " << a << ", b = " << b << endl;
}
void loopsOfNumbers(int n)
{
    while (n >= 0)
    {
        cout << n * n << endl;
        n = n - 1;
    }
}
int main(){
    //~~~~~~~~~~~ Loops and Numbers ~~~~~~~~~~~~~~~~~~~~~
    cout << "Enter a number: " << endl;
    int numbers;
    cin >> numbers;
    cout << endl;
    loopsOfNumbers(numbers);

    //~~~~~~~~~~~~ Swapping Numbers ~~~~~~~~~~~~~~~~~~~~~
     swapTwoNumbers();

    //~~~~~~~~~~~~ Adding Numbers ~~~~~~~~~~~~~~~~~~~~~~~
    cout<< "Let's perform some addition." << endl;
    cout << "Please enter the First number:" <<endl;
    int firstnum;
    cin >> firstnum;
    cout << "Please enter the Second number:" << endl;
    int secondnum;
    cin>>secondnum;
    addNumber(firstnum,secondnum);
    cout  << "The Sum of Two numbers is " << addNumber(firstnum,secondnum) << endl;
    return 0;
}


