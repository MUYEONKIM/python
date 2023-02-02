import numpy as np

a = [1,2,3,4,5,6,7,8,9,10]
b = np.array([1,2,3,4,5,6,7,8,9,10])

answer = []

for i in a :
    answer.append(i*2)

print(answer)
print(b*2)