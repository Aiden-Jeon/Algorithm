#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
	int n,rank[50001];
	pair<int,int> p[50001];
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>p[i].first;
		p[i].second = i;
	}
	sort(p,p+n);
	for(int i=0;i<n;i++)
		rank[p[i].second]=i;
	for(int i=0;i<n;i++)
		cout<<rank[i]<<' ';
}	