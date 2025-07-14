import matplotlib
matplotlib.use('TkAgg')

import heapq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 1) A* 맵 설정 & 탐색
grid = np.array([
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0]
])
start, goal = (0,0), (4,4)
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def heuristic(a,b): return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(grid,s,g): # s는 start, g는 goal 지점
    rows, cols = grid.shape
    open_set = []
    heapq.heappush(open_set, (heuristic(s,g),0,s))
    came_from, g_score = {}, {s:0} # g_score은 각 노드별로 지금까지의 최단거리를 저장. 여기서는 0
    visited = []

    while open_set:
        _, cost, cur = heapq.heappop(open_set) # heappop은 가장 작은 값을 가진 노드를 꺼냄. 여기서는 '가장 유망한 경로'. cur은 현재 탐색하는 경로를 의미
        if cur == g: # 목표지점에 도착한 순간인 마지막에만 1번 만족되는 조건
            path = []
            while cur in came_from:
                path.append(cur) # 최종 경로에 속한 근접 노드를 path에 저장
                cur = came_from[cur]
            path.append(s); path.reverse() # path가 역순으로 저장되어 있으므로 reverse() 사용
            return path, visited
            
        for dx, dy in dirs:
            nb = (cur[0]+dx, cur[1]+dy) # nb는 neighbor인 노드 의미함(여기서는 상하좌우)
            x,y = nb
            if 0 <= x < rows and 0 <= y < cols and grid[x,y] == 0:
                nc = g_score[cur]+1 # nc: 새로운 경로비용(nb까지의 잠정적인 최단거리. 즉, 현재 탐색하는 노드(cur)까지 걸린 거리 +1이다)
                if nb not in g_score or nc < g_score[nb]: # g_score에 해당 nb값이 없음 or 새로운 잠정적 최단거리 발견하면
                    g_score[nb] = nc
                    heapq.heappush(open_set,(nc+heuristic(nb,g),nc,nb))
                    came_from[nb] = cur
                    visited.append(nb)
    return None, visited # astar 알고리즘이 실패했을 때를 대비함. 어디까지 탐색했는지(visited)를 return

path, visited = a_star(grid,(0,0),(4,4))
frames = len(visited)+len(path)

#2) 컬러맵 정의(인덱스별 확실한 색으로)
# 0: 흰색, 1: 검은색, 2: 빨간색, 3: 파란색
cmap = ListedColormap(['white', 'black', 'red', 'blue'])

# 3) 인터렉티브 창
plt.ion() # 인터렉티브 모드(실시간)을 켜는 명령어
fig, ax = plt.subplots() # figure(전체 그림)
ax.set_title("A* Pathfinding")
ax.axis('on')
# 초기에 obstacle/free 반영
grid_int = grid.copy().astype(int) # 원본 grid를 보호하기 위해 copy를 생성한 후 데이터타입은 int로(색 구분 위해)
# grid_int를 2차원 배열로 해석한 후 색으로 표현
im = ax.imshow(grid_int, cmap=cmap, vmin=0, vmax=3) # 이때 내가 정의한 ListedColormap 사용. 색이 정확하게 매핑되도록 색 범위를 제한(0~3)
plt.show(block = False) # 창이 떠있는 동안에도 코드 계속 진행(block = True면 창이 떠있는 동안 코드 멈춤)
plt.pause(0.1) # 그림 보이도록 잠깐 멈춤

# 4) 수동 루프
# 사용 이유 1. Matplotlib의 기본 애니메이션이 Mac에서 잘 동작하지 않았음
# 사용 이유 2. visited(방문 노드, 빨간색)와 path(최단 경로) 표시 타이밍을 세밀하게 컨트롤하기 위해
for i in range(frames):
    frame = grid_int.copy() # 윗줄의 frame's'와 다름. 매번 새로운 화면 격자를 생성 <- 전 프레임의 변화가 영향을 주지 않도록
    # visited(방문) 노드 표시
    for k in range(min(i+1,len(visited))):
        x,y = visited[k]
        frame[x,y] = 2 # 빨간색으로 색칠
    # path(경로) 노드 표시
    if i >= len(visited):
        for k in range(i-len(visited)+1):
            x,y = path[k]
            frame[x,y] = 3
    im.set_data(frame)
    ax.set_xlabel(f"Frame {i}") # 프레임이 바뀌는지(애니메이션 동작 여부) 체크를 위해
    fig.canvas.draw()
    fig.canvas.flush_events() # 바뀐 data를 반영하는 기능. pause만 쓰는 것도 가능하나 안정성, 세밀한 타이밍 제어를 위해 flush_event() 사용
    plt.pause(0.3)

plt.ioff()
input("애니메이션 완료. Enter를 누르면 종료됩니다.") # 애니메이션이 끝난 후 그래프 창이 바로 닫히지 않게 하기 위함
