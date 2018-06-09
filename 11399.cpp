#include <iostream>
#include <algorithm>
using namespace std;
int main(void){
	ios::sync_with_stdio(false);
	int n,time[1000];
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>time[i];
	sort(time,time+n);
	int result=0;
	for(int i=0;i<n;i++)
		result += time[i]*(n-i);
	cout<<result;
}