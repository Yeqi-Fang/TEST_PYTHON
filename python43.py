import time
import numpy as np

lst = [i for i in range(10000000)]
tlist = []
for i in range(3):
    s = 0
    t1 = time.time()
    for i in lst:
        s+=i
    t2 = time.time()
    tlist.append(t2-t1)
print(s)
print(tlist)
print('Time Consumed:', np.mean(tlist))
