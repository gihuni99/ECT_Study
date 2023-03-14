#[입력 조건]

#1. 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다.(3≤N,M≤50)
#2. 둘째 줄에 게임 캐릭터가 있는 칸의 좌표(A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
#방향 d값은 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
#3. 셋째 줄부터 맵이 육지인지 바다인지 정보가 주어진다.
#0: 육지, 1:바다
#4. 처음 캐릭터가 위치한 칸의 상태는 항상 육지이다.

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)] # d[][]의 값이 1이면 방문한 것이다.
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리 / x가 행 방향, y가 열 방향

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split()))) # append() : 리스트 마지막에 요소 추가

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0] # dx=[-1].dy=[0]은 행이 하나 줄어드는 것이므로 북 방향 정의
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

