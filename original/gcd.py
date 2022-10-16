{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "32d7ebc4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter two integers separated by comma (,): 108,256\n",
      "By iterative gcd(108, 256) = 4\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "def gcd_by_iterative(a: int, b: int) -> int:\n",
    "    if(a == 0 and b == 0):\n",
    "        return 0\n",
    "    if (a == 0 or b == 0):\n",
    "        return a + b\n",
    "\n",
    "\n",
    "    u = int(math.copysign(1,a) * a)\n",
    "    v = int(math.copysign(1,b) * b)\n",
    "\n",
    "#   Let shift := lg K, where K is the greatest power of 2 dividing both u and v\n",
    "    shift = 0\n",
    "    while (((u | v) & 1) == 0):\n",
    "        u >>= 1\n",
    "        v >>= 1\n",
    "        shift+=1\n",
    "    while ((u & 1) == 0):\n",
    "        u >>= 1\n",
    "\n",
    "#   From here on, u is always odd\n",
    "    while (v != 0):\n",
    "#      Remove all factors of 2 in v as they are not common\n",
    "#      v is not zero, so while will terminate\n",
    "        while ((v & 1) == 0):\n",
    "            v >>= 1;\n",
    "\n",
    "#       // Now u and v are both odd. Swap if necessary so u <= v,\n",
    "        if (u > v):\n",
    "            t = v\n",
    "            v = u\n",
    "            u = t\n",
    "#       //Here v >= u and v - u is even\n",
    "        v -= u\n",
    "    \n",
    "    return u << shift;\n",
    "\n",
    "def main():\n",
    "    try:\n",
    "        nums = input(\"Enter two integers separated by comma (,): \").split(\",\")\n",
    "        num_1 = int(nums[0])\n",
    "        num_2 = int(nums[1])\n",
    "        print(f\"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}\")\n",
    "    except (IndexError, UnboundLocalError, ValueError):\n",
    "        print(\"Wrong input\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
