lineIn = lambda: [int(x) for x in input().split(" ")]

n = lineIn()[0]
a = lineIn()

a.sort()

mininum = a[0]

sos = "NO"

for i in range(1, n):
  if a[i] != mininum:
    sos = a[i]
    break

print(sos)
