lineIn = lambda : [int(x) for x in input().split(" ")]

def kfc_countdown():
  c = lineIn()[1]
  k_min = lineIn()[0]

  if c == 0 or k_min == 1:
    return 0

  if c < k_min:
    return c
  if c >= k_min:
    return k_min-1

T = lineIn()[0]
for t in range(T):
  print(kfc_countdown())
