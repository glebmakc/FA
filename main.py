#1 задача
import numpy as np
c=[]
cnt=1
cnt1=8
for i in range(11):
    data = list(np.arange(cnt, cnt1, 1))
    c.append(data)
    cnt=cnt+10
    cnt1=cnt+7
print(c)

#2 задача
import numpy as np
data = list(np.arange(2, 21, 2))
for i in range(len(data)):
    data[i]=data[i]*(data[i]+1)
print(data)

#3 задача
import numpy as np
data = np.random.randint(0, 11, (30,3))
data2 = np.random.randint(0, 11, (30,3))
cnt=0
for i in range(30):
    for j in range(3):
        if data[i][j]>data2[i][j]:
            cnt=cnt+data[i][j]
print(cnt)

#3 задача (2 вариант)
import numpy as np
data = np.random.randint(0, 11, (30,3))
data2 = np.random.randint(0, 11, (30,3))
print(sum(data[data > data2]))

#4 задача
n, m = int(input()), int(input())
print(np.array([[j % 2 if i % 2 == 0 else j % 2 + 2 for j in range(n)] for i in range(m)]))

#5 задача

import numpy as np
arr = np.random.randint(0, 11, (20,20))
print(arr)
c=[]
for i in range(1,20):
    c.append(arr[i-1][i])
print(c)

#6 задача

import numpy as np
import random
arr = ['Москва', 'Санкт-Петербург','Калуга','Казань','Иваново','Уфа','Владивосток','Суздаль','Мурманск','Ялта']
for i in range(100):
    print(arr[random.randint(0,9)])

#7 задача

import numpy as np
arr=np.zeros((8,8))
arr[1][:]=-1
arr[-2][:]=1
arr[0] = [-4, -3, -2, -6, -5, -2, -3, -4]
arr[-1] = [4, 3, 2, 6, 5, 2, 3, 4]
print(arr)

#8 задача
print(np.array(sorted(np.random.randint(0, 101, (20, 3)), key=lambda x: (x[0]**2 + x[1]**2+x[2]**2)**0.5)))

#9 задача
import numpy as np
c=[]
cnt=1
cnt1=8
for i in range(11):
    data = list(np.arange(cnt, cnt1, 1))
    c.append(data)
    cnt=cnt+10
    cnt1=cnt+7
print(c)

#10 задача

import numpy as np
arr = np.random.randint(0, 101, 20)
arr1= sorted(arr)
arr3 = list(arr)
arr2 = list(arr1)


print(arr3.index(arr2[-2]))

#11 задача
import numpy as np
def nearest(lst, target):
  return min(lst, key=lambda x: abs(x-target))

arr = np.random.randint(0, 101, 20)
n = int(input())
print(nearest(arr,n))
