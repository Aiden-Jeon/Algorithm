#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
	int n;
	pair<int,int> p[100];
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>p[i].first>>p[i].second;
	sort(p,p+n);
	for(int i=0;i<n;i++)
		cout<<p[i].first<<' '<<p[i].second<<endl;
}	