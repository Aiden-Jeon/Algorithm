#include <iostream>
using namespace std;
int main(void){
	int n,k,a[11],coin=0;
	
	cin>>n>>k;
	for(int i=1;i<=n;i++)
		cin>>a[i];
	while(k>0){
		if(a[n]<=k){
			coin += k/a[n];
			k = k%a[n];
		}
		n--;
	}
	cout<<coin;
}