#include <iostream>
using namespace std;
int main(void){
	int a,d,n;
	cin>>a;
	cin>>d;
	cin>>n;
	
	for(int i=1;i<n;i++){
		a += d;
	}
	cout<<a;
}