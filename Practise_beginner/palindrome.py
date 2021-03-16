x='abaabaca'

for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        sub=x[i:j+1]
        if sub==sub[::-1]:
            print(sub)