from bisect import bisect_left
 
lineIn = lambda: [int(x) for x in input().split()]
 
def binary_search_bisect(arr, x):
    i = bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1
 
def progressive_square():
  n, c, d = lineIn()
  temp = lineIn()
  b = []
  for t in temp:
    b.insert(bisect_left(b, t), t)
  d = abs(d)
  b_1_1 = b.pop(0)
  for i in range(1, n):
    find = binary_search_bisect(b, b_1_1+(c+d)*i)
    if find == -1:
      return False
    b.pop(find)
  
  for i in range(n):
    b_i_i = b_1_1+(c+d)*i
    for j in range(1, n-i):
      find = binary_search_bisect(b, b_i_i+d*j)
      if find == -1:
        return False
      b.pop(find)
 
      find = binary_search_bisect(b, b_i_i+c*j)
      if find == -1:
        return False
      b.pop(find)
  
  return True
 
T = lineIn()[0]
for t in range(T):
  print("YES" if progressive_square() else "NO")