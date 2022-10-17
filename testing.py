# import pytest
# import numpy as np
import copy
from mutants import m1, m2, m3
import gcd

# test cases
tc1 = [[36, 108]]
tc2 = [[18, 39]]
testcases = [tc1, tc2]

# number to be multiplied in follow-up test cases
followup = [3]

# original program (oracle)
p = gcd.gcd_by_iterative

# mutants
m1 = m1.gcd_by_iterative
m2 = m2.gcd_by_iterative
m3 = m3.gcd_by_iterative
mutants = [m1, m2, m3]
labels = ['m1', 'm2', 'm3']

# ............. TESTING WITH MT .............


# testing with MT using MR1
def test_withmt():
    for mutant, label in zip(mutants, labels):
        for testcase, fvalue in zip(testcases, followup):
            si = testcase
            fi = copy.copy(testcase)
            fi.append(fvalue)
            so = mutant(si)*fvalue
            fo = mutant(fi)
            if so == fo:
                result = '-'
            else:
                result = 'killed'
            print('Testing {} with test case {} using {}: {} ({} vs {})'.format(
                label, testcase, fvalue, result, so, fo))


# test with conventional method
# test_withoracle()

# test with MT
test_withmt()
