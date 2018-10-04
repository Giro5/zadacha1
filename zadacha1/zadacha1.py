data = open("data.txt", "r").readlines()
n = int(data[0].strip())
t = int(data[1].strip())
a = [int(data[2 + i].split()[0]) for i in range(n)]
b = [int(data[2 + i].split()[1]) for i in range(n)]

for i in range(n):
    a.append(int(data[2 + i].split()[0]))
    b.append(int(data[2 + i].split()[1]))

#r = [0]*(n+1+n+1)
#for i in range(0, n+1):
#    r[i] = t + sum(a[j] for j in range(0, i)) + sum(b[j] for j in range(i, n))

#r = [(t+sum(a[0:i])+sum(b[i:n])) for i in range(n+1)]
r = 0
p = "a0"
for i in range(n+1):
    if p[0] == "a":
        if t<a[0]:
            r += t
            p = b + str(i)
        else:

print("Все пути:",r,"\nМинимальный путь:", min(r))

#print("Минимальный путь:",min(list(int(open("data.txt","r").readlines()[1].strip())+sum(list(int(open("data.txt","r").readlines()[2+i].split()[0]) for i in range(int(open("data.txt","r").readlines()[0].strip())))[0:i])+sum(list(int(open("data.txt","r").readlines()[2+i].split()[1]) for i in range(int(open("data.txt","r").readlines()[0].strip())))[i:int(open("data.txt","r").readlines()[0].strip())]) for i in range(int(open("data.txt","r").readlines()[0].strip())+1))))
