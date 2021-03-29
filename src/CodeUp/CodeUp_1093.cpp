#include <iostream>
#include <vector>
using namespace std;

vector<int> v(24,0);
int main(void){
	int n,std;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>std;
		v[std]++;
	}
	for(int i=1;i<24;i++)
		cout<<v[i]<<' ';
}