# STRHH - Half of the half (problem from SPOJ)

'''
Given a sequence of 2*k characters, please print every second character from the first half of the sequence. Start printing with the first character.

Input

In the first line of input your are given the positive integer t (1<=t<=100) - the number of test cases. In the each of the next t lines, you are given a sequence of 2*k (1<=k<=100) characters.

Output

For each of the test cases please please print every second character from the first half of a given sequence (the first character should appear).

Example

Input:
4
your 
progress 
is 
noticeable

Output:
y
po
i
ntc
'''
def solve():
    input=[]
    count = raw_input()
    c=0
    while (c < int(count.strip()) ):
        line = raw_input()
        input.append(line.strip())
        c = int(c) +1

    for i in range(len(input)):
      l = len(input[i])/2
      print every_second_char(input[i][0:l])


def every_second_char(str):
     c=0
     l=[]
     for i in list(str):
         if c%2==0:
           l.append(i)
         c+=1
     return ''.join(l)


if __name__=='__main__':
        solve()
