import matplotlib.pyplot as plt
# import cv2

# a = cv2.imread(r"D:\multi_media\pic\Saved Pictures\v2-66856212a5b21b625405bc0713f91082_1440w.jpg")
# a = cv2.cvtColor(a, cv2.COLOR_RGB2BGR)
# plt.imshow(a)
# plt.show()
# cv2.imshow('a', a)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# from tkinter import N


def timeit(f):
    import time

    def fun(*arg, **kwargs):
        t1 = time.time()
        f(*arg, **kwargs)
        t2 = time.time()
        print('The excution velosity is:', 1/(t2-t1))

    return fun


@timeit
def t1(n):
    s = 0
    for i in range(n):
        s += i
    print(s)


@timeit
def t2(n):
    s = 0
    i = 0
    while i < n:
        s += i
        i += 1

    print(s)

#%%
# t1(100000000)
# t2(100000000)
import matplotlib.pyplot as plt
# print(plt.style.available)
plt.style.use('dark_background')
x = [i/100 for i in range(200)]
y = [x**2 for x in x]
plt.plot(x, y)
plt.show()

# %%
import seaborn as sns
df = sns.load_dataset('iris')