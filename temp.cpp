#include <iostream>
using namespace std;
int recursiveSum(int n){
	if(n==1) 
		return 1;
	else
		return n + recursiveSum(n-1);
}

int main(void){
	int n = 5,ret;
	ret=recursiveSum(n);
	cout<<ret;
}