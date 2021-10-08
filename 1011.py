# -*- coding: utf-8 -*-
t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    
    d = y - x # 주어진 처음 위치x와 목표 위치 y사이의 거리
    cnt = 0 # 목표위치 까지 이동하는데 필요한 공간이동 장치 작동 횟수
    m = 1 # 이동해야 할 거리에서 공간이동 장치 작동 횟수
        # cnt와 다른 점: m은 주어진 거리에서 공간이동 장치가 작동하는 횟수로, 거리가 1에서 n번까지 늘어날 때,
        # 작동 횟수는 짝수번 마다 1씩 증가하는 규칙이 있다. 따라서 m은 이 때 작동하는 공간이동 장치 작동 횟수이고, 
        # cnt는 이 m만큼의 공간이동 장치 작동 횟수가 필요로 하는 이동 거리 d 의 개수이다.
        '''
         ex)
        d = 1 -> 1 -> cnt = 1, m = 1
        d = 2 -> 11 -> cnt = 2, m = 1
        
        d = 3 -> 111 -> cnt = 3, m = 2
        d = 4 -> 121 -> cnt = 3, m = 2
        d = 5 -> 1211 -> cnt = 4, m = 2
        d = 6 -> 1221 -> cnt = 4, m = 2
        
        d = 7 -> 12211 -> cnt = 5, m = 3....
        
        
         즉, 주어진 거리를 이동할 때, 공간이동 장치 작동 횟수가 cnt이고,
        각 거리마다 해당 cnt와 같은 횟수만큼의 cnt를 가진 거리의 개수가 m이다.
        
        위 예시에서 처럼, cnt가 1인(공간이동 장치 작동 횟수가 1) 거리는 1 하나 이고,
        cnt가 2인(공간 이동 장치 작동 횟수가 2)거리는 2 하나 이다.
        반면에 cnt가 3인 거리는 3과 4, 2개 이고, cnt가 4인 거리는 5와 6으로 또한 2개이다.
        따라서, 이 규칙대로 거리마다 cnt를 구해서, 같은 cnt를 공유하는 거리의 개수를 m으로 묶어주면,
        1,1,2,2,3,3,4,4... 와 같은 규칙성을 보이며, m이 늘어남은 해당 cnt를 공유하는 거리가 1개씩 늘어남을
        의미 함으로, 주어진 거리에서 m을 계속 빼주면서(혹은 m을 계속 늘려서) 거리와 같아질 때까지 cnt를 1씩 더해주면
        해당 거리까지 도달하는데 필요한 공간이동 장치 작동 횟수를 구할 수 있다.
        
        '''
    total = 0 # 총 이동거리의 합
    
    while d > total:
        cnt += 1 # 공간이동 장치 작동 횟수
        total += m # 현재 이동거리를 더해줌
        if cnt % 2 == 0: # 위의 규칙성에 의해 cnt가 짝수번 째가 될 때 마다 장치 작동 횟수가 1씩 늘어남.
            m += 1
    print(cnt)
            