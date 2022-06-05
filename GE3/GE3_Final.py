import random
from time import time
import gmpy2
import pandas as pd


def isprime(x):
    for i in range(20):
        a = random.randrange(x)
        if pow(a, x, x) != a:
            return False
    return True


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def gen_prime(BITS):
    ub = 2**BITS
    lb = ub // 2
    p = random.randrange(lb, ub)
    while not isprime(p):
        p = random.randrange(lb, ub)
    return p


def fast_gen_prime_1(BITS):
    ub = 2**BITS
    ub = ub / 2
    lb = ub // 2
    r = random.randrange(lb, ub)
    p = 2*r + 1
    while not isprime(p):
        r = random.randrange(lb, ub)
        p = 2*r + 1
    return p


def fast_gen_prime_2(BITS):
    ub = 2**BITS
    ub = ub / 6
    lb = ub // 2
    r = random.randrange(lb, ub)
    p = 6*r + 1
    while not isprime(p):
        r = random.randrange(lb, ub)
        p = 6*r + 1
    return p


primelst = [2]
while primelst[-1] < 166:
    primelst.append(gmpy2.next_prime(primelst[-1]))

M = 1


def fast_gen_prime(BITS):
    ub = 2**BITS
    ub = ub / M
    lb = ub // 2
    r = random.randrange(lb, ub)
    p = M*r + 1
    while not isprime(p):
        r = random.randrange(lb, ub)
        p = M*r + 1
    return p


def GE3_A():
    print("Original Code")
    ts = time()
    for i in range(100):
        p = gen_prime(256)
    tm = time() - ts
    print("Time to generate 100 primes:", tm, "seconds")

    print("\nFast_gen_prime - scenario 1")
    ts1 = time()
    for i in range(100):
        p1 = fast_gen_prime_1(256)
    tm1 = time()-ts1
    print("Time to generate 100 primes:", tm1, "seconds")
    if tm - tm1 > 0:
        print(tm - tm1, "seconds faster than Original Code")
        print("{:.2f}".format(
            (tm-tm1)/tm1*100), "%", "faster than Original Code")
    elif tm - tm1 < 0:
        print(tm1 - tm, "seconds slower than Original Code")
        print("{:.2f}".format(
            (tm1-tm)/tm1*100), "%", "slower than Original Code")
    else:
        print("Same speed calculation as Original Code")

    print("\nFast_gen_prime - scenario 2")
    ts2 = time()
    for i in range(100):
        p2 = fast_gen_prime_2(256)
    tm2 = time()-ts2
    print("Time to generate 100 primes:", tm2, "seconds")
    if tm - tm2 > 0:
        print(tm - tm2, "seconds faster than Original Code")
        print("{:.2f}".format(
            (tm-tm2)/tm2*100), "%", "faster than Original Code")
    elif tm - tm2 < 0:
        print(tm2 - tm, "seconds slower than Original Code")
        print("{:.2f}".format(
            (tm2-tm)/tm2*100), "%", "slower than Original Code")
    else:
        print("Same speed calculation as Original Code")


def GE3_B():
    original = []
    for i in range(20):
        ts_1 = time()
        for j in range(100):
            p = gen_prime(256)
        original.append(time() - ts_1)

    list = []
    for i in range(20):
        M *= primelst[i]
        ts = time()
        for j in range(100):
            p = fast_gen_prime(256)
        list.append(time() - ts)

    dict_1 = {'steps': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                        12, 13, 14, 15, 16, 17, 18, 19, 20], 'time': original}
    dict_2 = {'steps': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                        12, 13, 14, 15, 16, 17, 18, 19, 20], 'time': list}
    df_1 = pd.DataFrame(dict_1)
    df_2 = pd.DataFrame(dict_2)
    df_1.to_csv('original.csv')
    df_2.to_csv('fast_gen_prime.csv')


# GE3_A()
# GE3_B()
