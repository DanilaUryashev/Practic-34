
print('Задание №1')
print('a:= ', end='')
a= int(input())
print('b:= ', end='')
b= int(input())
print('c:= ', end='')
c= int(input())
print('d:= ', end='')
d= int(input())
print(" ")
for i in range(c,d+1):
    print("\t", i, end="")
for i in range(a, b+1):
    print('\n', i, end="")
    for j in range(c, d+1):
        print('\t', i*j, end="")
print('')

print('Задание №2')
a=0
while True:
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        print(a)

print('Задание №3')
sum=0
while True:
    a = int(input())
    if a == 0:
        print(sum)
        break
    sum= sum+a

print('Задание №4')
print('Введите количество информатиков')
a=int(input())
print('Введите количество биологов')
b=int(input())
i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print(i)

print('Задание №5')
print('a= ',end='')
a=int(input())
print('b= ',end='')
b=int(input())
sum=0
i=0
while a<=b:
    sum=sum+a
    a=a+1
    i=i+1
print(sum/i)

print('Задание № 6')
a=input()
s1 = a.upper().count('c'.upper())
s2 = a.upper().count('g'.upper())
S=s1+s2
print(S/len(a)*100)

print('Задание № 7')
s = str(input())
l = len(s)-1
c = 1
t = ''
if len(s)==1:
    t = t +s+str(c)
else:
    for i in range(0,l):
        if s[i]==s[i+1]:
            c +=1
        elif s[i]!=s[i+1]:
            t = t + s[i]+str(c)
            c = 1
    for j in range(l,l+1):
        if s[-1]==s[-2]:
            t = t +s[j]+str(c)
        elif s[-1]!=s[-2]:
            t = t +s[j]+str(c)
            c = 1
print(t)

print('Задание № 8')
s = [ int(i) for i in input().split()]
summ = 0
l = len(s)-1
for i in range(0,l+1):
    summ = summ + s[i]
print(summ)

print('Задание №9')
s = [int(i) for i in input().split()]
t = []
l = len(s)-1
k = 0
i = 0
if len(s)==0:
    print(str(0))
else:
    for st in s:
        if len(s)>1:
            if i==0:
                k = s[i+1] + s[-1]
                t.append(k)
            elif i>0 and i<l:
                k=s[i-1]+s[i+1]
                t.append(k)
            elif i==l:
                k = s[i-1]+s[0]
                t.append(k)
        elif len(s)==1:
            k = s[i]
            t.append(k)
        i +=1
    j = 0
    for st2 in t:
        print(str(t[j])+' ',end='')
        j +=1

print('Задание №10')
s = [ int(i) for i in input().split()]
t = []
s.sort()
l = len(s)-1
k = 100000
if len(s)!=1:
    for i in range(0,l):
        if s[i]==s[i+1] and s[i]!=k:
            t.append(s[i])
            k=s[i]
    for j in range(l,l+1):
        if s[-1]==s[-2] and s[j]!=k:
            t.append(s[j])
n = len(t)
for g in range(0,n):
    print(t[g],end=' ')

print('Задание №11')
sum=0
sum2=0
while True:
    i=int(input())
    sum+=i
    sum2+=i**2
    if sum==0:
        break
print(sum2)

print('Задание №12')
print('n= ', end='')
n=int(input())
z=n
if n==1:
    print(1)
if n==2:
    print(12)
else:
    for i in range(1,n):
        for j in range(0,i):
            print(i,end='')
            z -= 1
            if z==0:
                break
        if z == 0:
            break

print('Задание №13')
print('Введите список чисел:')
list=input().split()
print('Найти число: ', end='')
xx=input()
for i in range(len(list)):
    if list[i]==xx:
        print(i)

print('Задание №14')
n = ''
m = []
print("Введите 'end' для остановки заполенения массива")
while True:
    n = str(input()) # ввод строк
    if n == 'end':
        break
    m.append([int(s) for s in n.split()])
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[(i+1) % li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]

for i in range (li):
    for j in range (lj):
        print(new[i][j], end =' ')
    print()
print('Задание №15')
def spiral(n):
    dx, dy = 1, 0
    x, y = 0, 0
    myarray = [[None] * n for j in range(n)]
    for i in range(1, n ** 2 + 1):
        myarray[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return myarray
def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print(myarray[x][y], end=' ')
        print()
n = int(input())
printspiral(spiral(n))

import math
print('Задание №16')
print('Введите стороны треугольника')
print('a= ',end='')
a=int(input())
print('b= ',end='')
b=int(input())
print('c= ',end='')
c=int(input())
p= (a+b+c)/2
S= math.sqrt(p*(p-a)*(p-b)*(p-c))
print(S)

print('Задание №17')
print('x= ', end='')
x=int(input())
if x<=12 and x>-15:
    print('True')
elif x>14 and x<17:
    print('True')
elif x>=19:
    print('True')
else:
    print('False')

print('Задание №18')
A = float (input())
B = float (input())
C = str (input())
if C =='+':
    print(A+B)
elif C=='-':
    print(A-B)
elif C=='*':
    print(A*B)
elif C=='/' and B==0:
    print("Деление на 0!")
elif C=='/' and B!=0:
    print(A/B)
elif C=='mod' and B==0:
    print('Деление на 0!')
elif C=='mod' and B!=0:
    print(A%B)
elif C=='pow':
    print(A**B)
elif C=='div' and B==0:
    print('Деление на 0!')
elif C=='div' and B!=0:
    print(A//B)

print('Задание №19')
a=int(input())
b=int(input())
c=int(input())
s = a + b + c;
print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))

print('Задание №20')
s = str(input())
if len(s)<6 or len(s)>6:
    print('Не верный номер билета')
    exit()
sum1=int(s[0])+int(s[1])+int(s[2])
sum2=int(s[3])+int(s[4])+int(s[5])
if sum1==sum2:
  print('Счастливый')
else:
  print('Обычный')