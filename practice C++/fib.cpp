#include <iostream>
#include  
using namespace std;


//////// START OF MARKER FOR fib


long long fib(int x)
{
  long long a;
  long long b;
  long long n;
  a = 0;
     b = 1;
    

    for (int i = 0; i< x; i++)
    {
        n = a + b;
        a = b;
        b = n;
        
    }
  return a;
}
//////// END OF MARKER 



//////// DO NOT MODIFY CODE BEYOND THIS LINE

int main(int argc, char* argv[]) {
    cout << (fib(atoi(argv[1]))) <
