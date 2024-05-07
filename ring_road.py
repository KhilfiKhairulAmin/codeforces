lineIn = lambda : [int(x) for x in input().split(" ")]

n = lineIn()[0]

graph = {}
init = None
for _ in range(n):
  a, b, c = lineIn()
  init = a
  if graph.get(a, None) == None:
    graph[a] = []
  graph[a].append((b, 0))
  if graph.get(b, None) == None:
    graph[b] = []
  graph[b].append((a, c))

# Traverse the graph clockwise and anti-clockwise
total_cost = [0, 0]
cur = init
for k in range(2):
  edge = graph[cur][k]
  for i in range(n):
    next_, cost = edge
    total_cost[k] += cost
    edge = list(filter(lambda x: x[0] != cur, graph[next_]))[0]
    cur = next_

print(min(total_cost))
