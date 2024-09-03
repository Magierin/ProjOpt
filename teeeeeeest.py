d = {'1': 7, '2': 8, '3': 9}
l = [1, 3, 2]
n = []

for i in range(len(l)):
    if str(l[i]) in d.keys():
        summe = l[i] * d.get(str(l[i]))
        print(summe)
        n.append(summe)
print(n)
