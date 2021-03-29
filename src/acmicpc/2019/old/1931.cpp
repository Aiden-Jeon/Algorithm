#include <iostream>
#include <algorithm>
using namespace std;
int main(void){
	ios::sync_with_stdio(false);
	pair<int,int> time[100000];
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>time[i].second>>time[i].first;
	sort(time,time+n);
	
	int end=time[0].first,result = 1;
	for(int i=1;i<n;i++){
		if(time[i].second>=end){
			result ++;
			end = time[i].first;
		}
	}
	cout<<result;

	return 0;
}