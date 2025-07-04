import heapq

# 맵 정의(0: 이동 가능, 1: 장애물)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

# 방향(directions) = 상, 하, 좌, 우
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    # 맨해튼 거리(대각선 거리는 계산하지 않음. 상하좌우 거리 계산) 사용
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    # heap에 시작 노드를 (예상 총 거리, 실제 거리, 현재 위치) 형태를 추가
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))

    came_from = {} # 경로 복원용
    g_score = {start: 0} # 시작점 ~ 현재 노드까지 누적 비용 저장하는 dict

    while open_set:
        _, curr_g, current = heapq.heappop(open_set) # 여기서 f(n)은 사용되지 않으므로 _로 표시

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current] # 직전 위치를 새로운 위치에 대입하여 (거꾸로 된) 지나온 경로를 구함.
            path.append(start)
            path.reverse()
            return path
        
        for dx, dy in dirs:
            neighbor = (current[0] + dx, current[1] + dy)
            x, y = neighbor
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0: # (x, y)가 map 안에 있고 장애물이 없는 공간이라면
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g # 경로의 누적 거리 저장
                    f_score = tentative_g + heuristic(neighbor, goal) # 누적 거리 + 휴리스틱
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor)) # open_set에 데이터 추가(예상 총 거리, 실제 거리, 현재 위치)
                    came_from[neighbor] = current # 현재 위치를 지나온 경로에 추가

    return None # 경로 X

# map 상황 그리기
def print_grid(grid, path, start, goal):
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[0])):
            pos = (i, j)
            if pos == start:
                row += "S "
            elif pos == goal:
                row += "G "
            elif grid[i][j] == 1:
                row += "█ " # 장애물
            elif pos in path:
                row += "* " # A* 알고리즘이 실제로 지나간 경로
            else:
                row += "· " # 이동 가능한 공간
        print(row)

# 실행
path = a_star(grid, start, goal)

#출력
if path:
    print("경로:", path)
    print() # 의미X, 가독성 위해
    print_grid(grid, path, start, goal)
else:
    print("경로를 찾을 수 없습니다.")