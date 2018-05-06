

#include <iostream>
#include 
using namespace std;

string to_stringx(const int& n);
void str2inta(string s, int x[], int size);
string inta2str(int x[], int size);


void array_sum(int a[], int b[], int c[], int size) {
  //////// START OF MARKER for array_sum code
	int i=0,carry=0;
	do
	{
		if(a[i]+b[i]<=9)
		{
			c[i]=a[i]+b[i];
		}
		else
		{
			c[i] = (a[i] + b[i]) % 10;
			carry = (a[i] + b[i]) / 10;
			a[i+1]=a[i+1]+carry;
		}
		i++;
	}while(i= 0; i--)
    val = val + to_stringx(x[i]);
  val = val.erase(0, val.find_first_not_of('0'));
  return val.length() > 0 ? val : "0";
}
string to_stringx(const int &n) {
  std::ostringstream stm ;
  stm << n ;
  return stm.str() ;
}


