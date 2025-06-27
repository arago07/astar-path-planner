# A* Path Planner (Console Version)

자율주행 로봇 경로 탐색 알고리즘 - 이 저장소는 A* 경로 탐색 알고리즘을 학습하기 위해 작성한 개인 프로젝트입니다.
알고리즘의 작동 원리를 이해하고 구현에 익숙해지기 위해, 기본 구조는 ChatGPT의 설명을 바탕으로 구성하고, 직접 타이핑하며 재구성하거나 일부 수정했습니다.

This repository is a personal learning project to understand the A* pathfinding algorithm.
The base structure was written based on explanations provided by ChatGPT, and I recreated and modified the implementation to reinforce my understanding through hands-on practice.

## Goal
- Python 으로 A* 알고리즘 수기 구현
- 2D 격자 맵에서 장애물을 피해서 목적지까지 최단 경로를 탐색하기
- 콘솔에 경로 출력하기

## Test Map Example
S . . . .

. # # # .

. . . # .

. # . . .

. . . # G

(S - start, G - goal, # - obstacle)

## Used Skills
- Python
- heapq(우선순위 큐)
- 휴리스틱: 맨해튼 거리

## Next Plan
- Day 2: 코드 구조 분리, 시각화 시작
- Day 3~: matplotlib, animation 기능 추가

## Result
