#include <cstdio>
#include <algorithm>  

int main(){
	int n;
	int max=0;
	double arr[1000];
	double avg;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%lf",&arr[i]);
		if (max < arr[i]) max = arr[i];
	}
	
	for(int i=0;i<n;i++){
		avg += (arr[i]/max)*100;
	}
	printf("%.2lf\n", avg/n);
}