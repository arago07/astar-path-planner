
# 🧭 A* Path Planner Simulator

자율주행 로봇 경로 탐색 알고리즘 - 이 저장소는 **A\* 경로 탐색 알고리즘**을 학습하기 위해 작성한 개인 프로젝트입니다.

알고리즘의 작동 원리를 이해하고 구현에 익숙해지기 위해, 기본 구조는 ChatGPT의 설명을 바탕으로 구성하고 직접 타이핑하며 재구성하거나 일부 수정했습니다.

> This repository is a personal learning project to understand the A* pathfinding algorithm.  
> The base structure was written based on explanations provided by ChatGPT, and I recreated and modified the implementation to reinforce my understanding through hands-on practice.

---

## ✅ Features

- **Day 1:** Console-based A* algorithm implementation  
- **Day 2:** Animated A* pathfinding visualization using `matplotlib`

---

## 📂 Project Structure

```txt

astar-path-planner-simulator/
├── day1_console_astar/
│ └── main.py # Text-based path planning on a grid
├── day2_visual_astar/
│ ├── main.py # Visual animation using matplotlib
│ ├── test2.py # Temporary test file
│ └── main.loop.py # Alternate testing version
├── map_sample.txt
└── README.md

```


---

## 🎯 Goal

- A\* 알고리즘을 단계별로 공부하기  
- 장애물을 피해서 목적지까지 최단 경로 탐색하기  
- 콘솔 및 시각화 결과로 경로 출력하기  
- `matplotlib`을 사용하여 시각적으로 검색 과정 이해하기  

---

## 🧪 Test Map Example

```
S . . . .
. # # # .
. . . # .
. # . . .
. . . # G

```

- `S`: Start
- `G`: Goal
- `#`: Obstacle

---

## 🛠 Technologies Used

- Python 3.x  
- `heapq` – for priority queue  
- `numpy` – for grid and map logic  
- `matplotlib` – for Day 2 animation  

---

## 🚀 How to Run

### 🔹 Day 1 – Console Version

```bash
cd day1_console_astar
python main.py
Expected output: 경로 및 방문 노드가 텍스트로 출력됩니다.

```

### 🔹 Day 2 – Visualization Version
1. Install dependencies

```bash
pip install matplotlib numpy

```

2. (macOS일 경우) main.py 내 백엔드 설정

```python

import matplotlib
matplotlib.use('TkAgg')

```

3. Run
```bash

cd day2_visual_astar
python main.py

```
Expected output: 애니메이션으로 노드 탐색 과정과 최종 경로가 시각화됩니다.

## 📌 Result
콘솔 버전에서는 텍스트 기반 경로 출력으로 A* 알고리즘의 흐름을 확인할 수 있습니다.

시각화 버전에서는 실제 경로 탐색 과정을 실시간으로 애니메이션으로 확인할 수 있어 직관적인 이해가 가능합니다.

ListedColormap을 활용해 방문 노드, 경로, 장애물을 구분된 색상으로 표현했습니다.

## 🙋‍♀️ Author
Go Ara (고아라)
학습용 개인 프로젝트이며, 경로 탐색 알고리즘과 시각화를 통해 Python 및 AI 관련 백엔드 개발에 대한 이해를 확장하고자 했습니다.

GitHub: @arago07


