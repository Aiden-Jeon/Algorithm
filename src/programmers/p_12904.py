s = 'aaaaa'

max_val = 1
for i in range(len(s)):
	for j in range(i+1,len(s)+1):
		if s[i:j] == s[i:j][::-1]:
			max_val = max(len(s[i:j]),max_val)
print(max_val)
