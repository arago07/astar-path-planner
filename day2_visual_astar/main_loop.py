import matplotlib
matplotlib.use('TkAgg')        # ← 대소문자 꼭 이대로!

import heapq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 1) A* 맵 설정 & 탐색 (기존 그대로)
grid = np.array([
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0]
])
start, goal = (0,0),(4,4)
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
def heuristic(a,b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
def a_star(grid, s, g):
    rows,cols = grid.shape
    open_set = []
    heapq.heappush(open_set,(heuristic(s,g),0,s))
    came_from, g_score = {}, {s:0}
    visited = []
    while open_set:
        _, cost, cur = heapq.heappop(open_set)
        if cur == g:
            path=[]
            while cur in came_from:
                path.append(cur)
                cur = came_from[cur]
            path.append(s); path.reverse()
            return path, visited
        for dx,dy in dirs:
            nb=(cur[0]+dx, cur[1]+dy)
            x,y=nb
            if 0<=x<rows and 0<=y<cols and grid[x,y]==0:
                nc = g_score[cur]+1
                if nb not in g_score or nc<g_score[nb]:
                    g_score[nb]=nc
                    heapq.heappush(open_set,(nc+heuristic(nb,g),nc,nb))
                    came_from[nb]=cur
                    visited.append(nb)
    return None, visited

path, visited = a_star(grid, (0,0), (4,4))
frames = len(visited) + len(path)

# 2) 컬러맵 정의 (인덱스별 확실한 색)
# 0:white, 1:black, 2:red, 3:blue
cmap = ListedColormap(['white','black','red','blue'])

# 3) 인터랙티브 창
plt.ion()
fig, ax = plt.subplots()
ax.set_title("A* Pathfinding")
ax.axis('on')

# 초기에 obstacle/free 반영
grid_int = grid.copy().astype(int)  
im = ax.imshow(grid_int, cmap=cmap, vmin=0, vmax=3)
plt.show(block=False)
plt.pause(0.1)

# 4) 수동 루프
for i in range(frames):
    frame = grid_int.copy()
    # 방문 노드 표시(2)
    for k in range(min(i+1, len(visited))):
        x,y = visited[k]
        frame[x,y] = 2
    # 경로 노드 표시(3)
    if i >= len(visited):
        for k in range(i - len(visited) + 1):
            x,y = path[k]
            frame[x,y] = 3

    im.set_data(frame)
    ax.set_xlabel(f"Frame {i}")
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.3)

plt.ioff()
input("▶ 애니메이션 완료—엔터 누르면 종료")