import sys 
q = lambda:sys.stdin.readline().strip()
t = []
for _ in range(int(q())):
	s_t,e_t = q().split()
	t.append([int(e_t),int(s_t)])
	

#end / start
t = sorted(t)
e_t = t[0][0]
time = 1
for i in range(1,len(t)):
	if t[i][1]>=e_t :
		time +=1
		e_t = t[i][0] 
		s_t = t[i][1] 
		#print(s_t,e_t)
#print(t)
print(time)