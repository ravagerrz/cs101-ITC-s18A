#include <iostream>
using namespace std;
#include <cmath>

int fac(long n){
	double long var = 1;
	for (long i = 1 ; i < n + 1 ; i++ ){
	var = var * i;
}
	return var;
}
double long sin2(long x,long y = 60 ){
	double long  var2 = 0.0;
	//double long var3;
	x = x * M_PI/180;
	for (double long k = 0;k < y ; k++){
		var2 +=  ((pow(-1,k))* (pow(x,(2*k)+1)))/fac((2*k)+1);
	}
	//var3 = ceil( var2);
	return var2;
	}


int main(){
	cout << sin2(30);

	return 0;
}
