from cProfile import label
import random
import matplotlib.pyplot as plt


def isprime(x):
    for i in range(20):
        a = random.randrange(x)
        if pow(a, x, x) != a:
            return False
    return True


r_bit = []
x_bit = []


def bit_calc(BITS, x):
    ub = 2**BITS
    ub = ub / x
    lb = ub // 2
    r = random.randrange(lb, ub)
    p = x*r + 1
    while not isprime(p):
        r = random.randrange(lb, ub)
        p = x*r + 1
    # print("x =", x, "\tBits ---> r:", r.bit_length(), "-- x:",
        # x.bit_length(), "-- p:", p.bit_length())
    r_bit.append(r.bit_length())
    x_bit.append(x.bit_length())
    return p


for i in range(1, 100):
    bit_calc(256, i)

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.plot(x_bit, label="x bits")
ax2.plot(r_bit, label="r bits")
ax1.set_xlabel("x (decimal)")
ax2.set_xlabel("x (decimal)")
ax1.set_ylabel("x (bits)")
ax2.set_ylabel("r (bits)")
ax1.legend()
ax2.legend()
plt.show()
