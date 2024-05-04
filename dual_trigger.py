lineIn = lambda : int(input())

def dual_trigger():
  n = lineIn()
  b = input()

  count_0 = b.count("0")
  if count_0 == n:
    return True
  if n == 1 or n == 2:
    return False
  count_1 = n - count_0
  if count_1 % 2 == 1:
    return False
  if count_1 == 2:
    pos = []
    for i in range(n):
      if b[i] == "1":
        pos.append(i)
    if pos[1] - pos[0] == 1:
      return False
  return True

T = lineIn()

for t in range(T):
  print("YES" if dual_trigger() else "NO")
