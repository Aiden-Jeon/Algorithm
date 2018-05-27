#include <cstdio>

int ratio(int arr[],int n,int sum){
	double avg;
	int cnt = 0;
	avg = sum / n;
	for(int i=0;i<n;i++) if(arr[i]>avg) cnt ++;
	printf("%.3lf%\n", (double)(cnt*100)/n);
}

int main(){
	int T;
	scanf("%d",&T);

	for(int t=0;t<T;t++){
		int n=0,sum=0;
		int arr[1000];
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d",&arr[i]);
			sum = sum + arr[i];
		}	
		ratio(arr,n,sum);
	}
}
