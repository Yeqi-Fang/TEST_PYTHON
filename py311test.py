import random
lst = [0, 1]
def timer(f):
    import time
    def inner(*args, **kwargs):
        t1 = time.perf_counter()
        f(*args, **kwargs)
        t2 = time.perf_counter()
        print("the executed time is:", t2-t1)

    return inner



@timer
def test1():
    for _ in range(int(1e7)):
        t = random.choice(lst)
        try:
            a = 1/1
        except:
            pass

@timer
def test2():
    for i in range(int(1e7)):
        a = 1


if __name__ == '__main__':
    test1()