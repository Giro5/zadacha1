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

#print("Все пути:",r,"\nМинимальный путь:", min(r))

r = 0
p = "a0"
for i in range(n):
    if p[0] == "a":
        if i != n - 1:
            if a[i] > b[i] + t:
                r += t + b[i]
                p = "b" + str(i + 1)
            elif a[i] < b[i] + t:
                r += a[i]
                p =  "a" + str(i + 1)
        else:
             if a[i] + t > b[i] + t:
                r += t + b[i]
                p = "b" + str(i + 1)
             elif a[i] + t < b[i] + t:
                r += a[i] + t
                p =  "a" + str(i + 1)
    elif p[0] == "b":
        if b[i] > a[i] + t:
            r += t + a[i]
            p = "a" + str(i + 1)
        elif b[i] < a[i] + t:
            r += b[i]
            p = "b" + str(i + 1)
    #print(p, r)

print("Минимальный путь:", r)

#print("Минимальный путь:",min(list(int(open("data.txt","r").readlines()[1].strip())+sum(list(int(open("data.txt","r").readlines()[2+i].split()[0]) for i in range(int(open("data.txt","r").readlines()[0].strip())))[0:i])+sum(list(int(open("data.txt","r").readlines()[2+i].split()[1]) for i in range(int(open("data.txt","r").readlines()[0].strip())))[i:int(open("data.txt","r").readlines()[0].strip())]) for i in range(int(open("data.txt","r").readlines()[0].strip())+1))))
