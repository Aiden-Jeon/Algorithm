#include <cstdio>
int add(int n){
	if(n==1) return 1;
	return n + add(n-1);
}

int main(){
	int n;
	scanf("%d",&n);
	printf("%d\n",add(n));
}