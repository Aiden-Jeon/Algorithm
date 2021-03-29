import sys
n = int(sys.stdin.readline())
n_arr = sys.stdin.readline().strip().split()
m = int(sys.stdin.readline())
m_arr = sys.stdin.readline().strip().split()

n_dict = {}
for i in n_arr:
	n_dict[i]=1

for i in m_arr:
	try:
		print(n_dict[i])
	except:
		print(0)
