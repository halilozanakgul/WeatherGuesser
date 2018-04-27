import csv
import math

T = []
Tt = []
date = []

with open("data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',', quotechar='"')
    for row in reader:
        if(row[0]!='STATION'):
            T.append(float(row[3]))
            date.append(row[2])

#t = n0 + n1*t1 + n2*t2 + n3*t3 + n4*t4 + n5*t5

n = [0.75, 1, 1, 1, 1, 1]

N = len(T)
Nt = int(N/10)
N -= Nt

T = [x/25 for x in T]

alpha = 0.0001

def calcMSE():
    ae = 0
    for i in range(5, N):
        ae += ((T[i] - (n[0] + n[1]*T[i-1] + n[2]*T[i-2] + n[3]*T[i-3] + n[4]*T[i-4] + n[5]*T[i-5]))**2)/N
    return math.sqrt(ae)

def calDer(x):
    res = 0
    for i in range(5,N):
        res += -T[i-x]*(T[i]-(n[0] + n[1]*T[i-1] + n[2]*T[i-2] + n[3]*T[i-3] + n[4]*T[i-4] + n[5]*T[i-5]))
    return res;

def calDer1():
    res = 0
    for i in range(5,N):
        res += -(T[i]-(n[0] + n[1]*T[i-1] + n[2]*T[i-2] + n[3]*T[i-3] + n[4]*T[i-4] + n[5]*T[i-5]))
    return res;

def calError():
    ave = 0
    for i in range(N,N+Nt):
        ave += abs(T[i] - (n[0] + n[1]*T[i-1] + n[2]*T[i-2] + n[3]*T[i-3] + n[4]*T[i-4] + n[5]*T[i-5]))/Nt
        print(
            "%.2f %.3f" % (T[i], (n[0] + n[1]*T[i-1] + n[2]*T[i-2] + n[3]*T[i-3] + n[4]*T[i-4] + n[5]*T[i-5])),
            T[i] - (n[0] + n[1]*T[i-1] + n[2]*T[i-2] + n[3]*T[i-3] + n[4]*T[i-4] + n[5]*T[i-5])
        )
    print(ave)

"""
while abs(calDer(1))>0.01:
    nn = [0, 0, 0, 0, 0, 0]
    nn[0] = n[0] - alpha*calDer1()
    for j in range(1, 6):
        nn[j] = n[j] - alpha*calDer(j)

    n = nn
    #print(n, calcMSE())
"""

n = [0.025721993180673964, 0.7295744826618324, -0.0672309715502604, 0.11744543302665661, 0.044112288076320394, 0.12862599813770678]
n[0] *= 25
T = [x*25 for x in T]

calError()
print(n)
