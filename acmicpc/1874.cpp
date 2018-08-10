#include <cstdio>

int main(){
	int t,top,n;
	scanf("%d",&t);
	char a[50];
	
	while(t--){
		top = 0;
		scanf("%s",a);
		for(int i=0;a[i]!=0;i++){
			if(a[i]=='(')
				top++;
			else
				top--;
				if(top<0) break;	
		}
		printf("%s\n",top==0?"YES":"NO");
	}
}