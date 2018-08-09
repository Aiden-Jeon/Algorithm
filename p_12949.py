arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]	
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

answer = []
for i in range(len(arr1)):
    temp=[]
    for j in range(len(arr2[0])):
        s = 0
        for k in range(len(arr1[0])):
            s += arr1[i][k]*arr2[k][j]
        temp.append(s)
    answer.append(temp)
print(answer)
