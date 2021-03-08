n=input()
num=[]
for i in range(len(n)):
    num.append(int(n[i]))
    
num = sorted(num)

for i in range(len(num)):
    print(num[i], end='')
print()
