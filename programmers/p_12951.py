import sys
s = sys.stdin.readline()

s = s.lower()
for i in range(len(s)-1):
	if i==0:
		t = s[i].lower()
		if ord(t)>=ord('a') and ord(t) <= ord('z'):
			s = t.upper() + s[1:]
	if s[i] == ' ':
		s = s[:i+1] + s[i+1].upper() + s[i+2:]
print(s)