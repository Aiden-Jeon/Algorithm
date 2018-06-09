#include <iostream>
using namespace std;
int main(void){
	int num,result=0;
	int i =0;

	cin>>num;
	while(1){
		if(result>=num){
			cout<<i;
			break;
		}
		else{
			i++;
			result+=i;
		}	
	}
}