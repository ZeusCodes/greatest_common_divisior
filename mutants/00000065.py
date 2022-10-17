import math


def gcd_by_iterative(a: int, b: int) -> int:
    if (a == 0 and b == 0):
        return 0
    if (a == 0 or b == 0):
        return a + b

    u = int(math.copysign(1, a) * a)
    v = int(math.copysign(1, b) * b)

#   Let shift : lg K, where K is the greatest power of 2 dividing both u and v
    shift = 0
    while (((u | v) & 1) == 0):
        u >>= 1
        v >>= 1
        shift += 1
# ORIGINAL CODE:
 #    while ((u & 1) == 0):
# MODIFIED TO:
    while((u & 1)<=0):
        u >>= 1

#   From here on, u is always odd
    while (v != 0):
        #      Remove all factors of 2 in v as they are not common
        #      v is not zero, so while will terminate
        while ((v & 1) == 0):
            v >>= 1

#       // Now u and v are both odd. Swap if necessary so u less than equal to v,
        if (u > v):
            t = v
            v = u
            u = t
#       //Here v more than equal to u and v minus u is even
        v -= u

    return u << shift


if __name__ == "__main__":
    import argparse
    params = argparse.ArgumentParser()
    params.add_argument('-num1', nargs="+", type=int, default=0)
    params.add_argument('-num2', nargs="+", type=int, default=0)
    args = params.parse_args()
    num_1 = args.num1[0]
    num_2 = args.num2[0]
    try:
        print(
            f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}")
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong input")

