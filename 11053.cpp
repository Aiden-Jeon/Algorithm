#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
	int N,arr[1000],count[1000],answer=1;
	cin>>N;
	for(int i=0;i<N;i++)
		cin>>arr[i];
	
	for(int i=0;i<N;i++){
		count[i] = 1;
		for(int j=0;j<i;j++){
			if(arr[j]<arr[i] && count[i] < count[j] +1){
				count[i] = count[j] +1;
				answer = max(count[i],answer);
			}
		}
	}
	cout<<answer;
}