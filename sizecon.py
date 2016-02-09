# SIZECON - Size Contest

'''
Given the set of integers, find the sum of all positive integers in it. Solutions can be sent in any language supported by SPOJ except Whitespace.
Input

t – number of test cases [t < 1000]
On each of next t lines given a integer N [-1000 <= N <= 1000]

Output

One integer equals to sum of all positive integers.

Score

Score equals to size of source code of your program except symbols with ASCII code <= 32.

Example

Input:
4
5
-5
6
-1
Output:
11
'''

import sys

def solve():
    input=[]
    t = sys.stdin.readline()
    c=0
    while (c < int(t.strip()) ):
        line = sys.stdin.readline()
        input.append(line.strip())
        c = int(c) +1
    sum=0
    for i in range(len(input)):
        if int(input[i]) > 0:
                sum = sum + int(input[i])
    print sum

if __name__=='__main__':
        solve()
