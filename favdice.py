# FAVDICE - Favorite Dice (form SPOJ)

'''
BuggyD loves to carry his favorite die around. Perhaps you wonder why it's his favorite? Well, his die is magical and can be transformed into an N-sided unbiased die with the push of a button. Now BuggyD wants to learn more about his die, so he raises a question:

What is the expected number of throws of his die while it has N sides so that each number is rolled at least once?

Input

The first line of the input contains an integer t, the number of test cases. t test cases follow.

Each test case consists of a single line containing a single integer N (1 <= N <= 1000) - the number of sides on BuggyD's die.

Output

For each test case, print one line containing the expected number of times BuggyD needs to throw his N-sided die so that each number appears at least once. The expected number must be accurate to 2 decimal digits.

Example

Input:
2
1
12

Output:
1.00
37.24
'''

'''
Mathematical solution :

The expected wait for all scores to appear = expected wait for one score + expected wait for second score + ... + expected wait for sixth and final score.  The probabilities of these events are, respectively, 6/6, 5/6, 4/6, 3/6, 2/6, 1/6.

Lemma

The expected wait, E, for an event of probability p, is 1/p.
Proof

Either the event occurs on the first trial with probability p, or with probability (1-p) the expected wait is 1 + E.
Therefore E = p.1 + (1 - p)(1 + E), from which E = 1/p.
(Notice that we have implicitly assumed that E is finite)

Therefore the expected wait for all scores to appear = 6/6 + 6/5 + 6/4 + 6/3 + 6/2 + 6/1 = 14.7.
'''

import sys

def solve():
    input=[]
    count = sys.stdin.readline()

    c=0
    while (c < int(count.strip()) ):
        line = sys.stdin.readline()
        input.append(line.strip())
        c = int(c) +1

    for i in range(len(input)):
        print "%.2f" %wait(int(input[i]))


def wait(p):
    num=0
    for i in range(p):
         num = num + (p/float(i+1))
    return num

if __name__=='__main__':
        solve()

