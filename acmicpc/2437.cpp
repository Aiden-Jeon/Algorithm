#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	int N,arr[1000],result=0;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>arr[i];
	}
	sort(arr,arr+N);
	if (arr[0]==0)
		cout<<1;
	else{
		for(int i=0;i<N && result+1>=arr[i];i++){
			result += arr[i];
		}
		cout<<result+1;
	}
		

}