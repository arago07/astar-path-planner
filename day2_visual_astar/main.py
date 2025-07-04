import matplotlib
matplotlib.use('TkAgg') # MacOSX라는 기본 백엔드가 애니메이션 기능과 충돌 일으키는 것 방지

import heapq
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# -------- 기본 A* 맵 설정 ---------
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0], 
    [0, 0, 0, 1, 0], 
    [0, 1, 0, 0, 0], 
    [0, 0, 0, 1, 0]
]
grid = np.array(grid) # 다중 리스트를 numpy 배열(ndarray) 형태로 변환 <- 빠른 성능, 효율적 메모리 사용

start = (0, 0)
goal = (4, 4)
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# --------- Hueristic -----------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# --------- A* 알고리즘 -----------
def a_star(grid, start, goal):
    rows, cols = grid.shape # numpy 배열에서 사용하는 속성 .shape를 사용해 배열의 크기 구하기
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start)) # (예상 거리, 실제 거리, 현재 위치)
    came_from = {}
    g_score = {start: 0}
    visited_order = [] # 탐색 과정을 의미함(최종경로X). 시각화용.

    while open_set:
        _, curr_g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, visited_order
        
        for dx, dy in dirs:
            neighbor = (current[0] + dx, current[1] + dy)
            x, y = neighbor # 지금 노드와 연결된 후보 노드
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]: # 지금 계산한 g값(새로 계산)이 이전에 알고 있던 값(지금까지 가장 짧은 비용)보다 작다면
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor))
                    came_from[neighbor] = current
                    visited_order.append(neighbor)

    return None, visited_order

# -------------- 시각화 애니메이션 ---------------

path, visited = a_star(grid, start, goal)
frames = len(visited) + len(path)

# --- 2. Figure & Image 셋업 ---
plt.ion()                       # interactive on
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='gray_r', vmin=0, vmax=1)
ax.set_title("A* Pathfinding")
ax.axis('on')                   # 축 켜기

plt.show()

# --- 3. 수동 루프 애니메이션 ---
for i in range(frames):
    # 3.1 원본 복사
    frame = grid.copy()

    # 3.2 방문 노드 표시
    for k in range(min(i+1, len(visited))):
        x,y = visited[k]
        frame[x,y] = 0.5

    # 3.3 경로 노드 표시 (방문 끝난 뒤)
    if i >= len(visited):
        for k in range(i - len(visited) + 1):
            x,y = path[k]
            frame[x,y] = 0.2

    # 3.4 이미지 업데이트 & redraw
    im.set_data(frame)
    fig.canvas.draw_idle()
    plt.pause(0.2)  # 0.2초마다 갱신

# 애니메이션 종료 후
plt.ioff()
input("▶ 완료! 엔터 누르면 종료")  # 창이 바로 닫히지 않도록
