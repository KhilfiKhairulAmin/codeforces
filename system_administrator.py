lineIn = lambda: [int(x) for x in input().split(" ")]

n, m, v = lineIn()

m_v = (n-1)*(n-2) / 2 + 1

# Determine if possible or not
if m > m_v:
  print(-1)
else:
  verts = [x for x in range(1, n+1)]

  # Make v the first elem
  temp = verts[0]
  verts[0] = verts[v-1]
  verts[v-1] = temp

  # Connect to a singular node
  print(v, verts.pop())
  m -= 1
  n -= 1

  # Connect to all other possible diagonals of n-1 other vertices
  counter = 1
  while m != 0:
    if counter % n == 0:
      verts.pop(0)
      counter = 1
      n -= 1
    print(verts[0], verts[counter])
    counter += 1
    m -= 1
