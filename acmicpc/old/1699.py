import sys
N = int(sys.stdin.readline().strip())

dp = [0]*(N+1)


for i in range(1,N+1):
	for j in range(1,N+1):
		if j*j > N+1:
			break
		if i - j*j >=0:
			if dp[i]>dp[i-j*j]+1 or dp[i]==0:
				dp[i] = dp[i-j*j]+1
print(dp[-1])