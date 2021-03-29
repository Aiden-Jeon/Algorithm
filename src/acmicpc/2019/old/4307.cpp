#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	int T,l,n,Long,Short;
	
	cin>>T;
	int a;
	while(T--){
		Long=Short=0;
		cin>>l>>n;
		for(int i=0;i<n;i++){
			cin>>a;
			Long = max(Long,max(a,l-a));
			Short = max(Short,min(a,l-a));
		}
		cout<<Short<<' '<<Long<<endl;
	}

}