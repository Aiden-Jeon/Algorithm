import sys
strings = sys.stdin.readline().strip().split(',')
strings.sort()
n=1
print(strings)
my_dict = []

for i,j in enumerate(strings):
	my_dict.append((j[n],i))
my_dict.sort()

result = []
for i,j in my_dict:
	result.append(strings[j])

print(result)