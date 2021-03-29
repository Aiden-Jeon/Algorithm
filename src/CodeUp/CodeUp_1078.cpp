#include <iostream>
using namespace std;
int main(void){
	int num;
	int result=0;
	cin>>num;
	for(int i=1;i<=num;i++){
		if(i%2==0)
			result += i;
	}
	cout<<result<<endl;
}