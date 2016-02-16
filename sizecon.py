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
def solve():
    t = raw_input()
    c=0
    sum=0
    while (c < int(t.strip()) ):
        line = raw_input()
        if int(line.strip()) >0:
            sum = sum + int(line.strip())
        c = int(c) +1
    print sum

if __name__=='__main__':
        solve()
