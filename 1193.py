# -*- coding: utf-8 -*-
x = 9

a = 0 # 초기값
line = 1 # 분수 표에서 x번째 분수가 위치한 대각선 라인

for i in range(1, x + 1):
    a += i # 초기값 a에 각 라인에 해당하는 원소의 수만큼 더해줌
    if a >= x:
        break
    else:
        line += 1 # x가 해당 라인에 없으면 line을 1만큼 늘려 줌
        
print(a, b)
b = a - x
if line % 2 == 0: # x가 위치한 라인이 짝수번 째 라인일 때 (좌하향)
    print(f'{line - b}/{b + 1}')
else: # x가 위치한 라인이 홀수번 째 라인일 때 (우상향)
    print(f'{ (b + 1)}/{line - b}')