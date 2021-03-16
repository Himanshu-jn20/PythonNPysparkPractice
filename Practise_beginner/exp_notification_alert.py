import math


nd=list(map(int, input().rstrip().split()))
n,d = nd
med=d/2
mod=d%2

med_val=math.floor(med)


exp_main=list(map(int, input().rstrip().split()))
exp=exp_main[0:d]
exp.sort()
notification=0
for i in range(n-d):
    if i>0:
        exp.pop(0)
        k=0
        for j in range(d-1):
            if exp_main[d+i-1] < exp[j]:
                exp.insert(j,exp_main[d+i-1])
                k=1
                break
        if k == 0:
            exp.append(exp_main[d+i-1])
                
        
    if mod != 0:
        lim=2 * exp[med_val]            
    else:
        lim=2 * (exp[med_val-1] + exp[med_val])/2
    
    if int(exp_main[d+i]) >= lim:
            notification=notification+1

print(notification)