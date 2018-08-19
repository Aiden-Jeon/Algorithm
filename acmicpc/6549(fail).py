import sys

while True:
	temp = list(map(int,sys.stdin.readline().strip().split()))
	if temp == [0]:
		break
	min_i,idx = min((v,i) for i,v in enumerate(temp))
	max_s = min_i*len(temp)
	
	if idx == 0 :
		node = [(1,len(temp)-1)]
	elif idx == len(temp)-1:
		node = [(0,len(temp)-2)]
	else:
		node = [(0,idx-1),(idx+1,len(temp)-1)]
	
	for left,right in node:
		if left == right:
			max_s = max(max_s,temp[left])
		else:
			min_i,idx = min((v,i) for i,v in enumerate(temp[left:right+1]))
			max_i = max(temp[left:right+1])
			idx += left
			if idx == right:
				node.append((left,idx-1))
				max_s = max(max_s,temp[right],min_i*(right-left+1))
				
			elif idx == left:
				node.append((idx+1,right))
				max_s = max(max_s,temp[left],min_i*(right-left+1))
				
			else:
				node.append((left,idx-1))
				node.append((idx+1,right))
				max_s = max(max_s,min_i*(right-left+1))
				
	print(max_s)
		