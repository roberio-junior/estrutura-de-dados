from collections import deque
fila = deque([])
fila.append(5)
fila.append(10)
fila.append(9)
while (len(fila) > 0):
    e = fila.popleft()
    print(e)