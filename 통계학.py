'''
n = int(input())

num_list = []

for i in range(n):
    num_list.append(int(input()))
    
print(round(sum(num_list) / n)) # 산술평균

print(sorted(num_list)[n // 2]) # 중앙값

st, dic = set(num_list), dict()

for i in st:
    dic[i] = num_list.count(i)
    

maximum = max(dic.values())

dic = sorted(dic.items())

li = []

for i, j in enumerate(dic):
    if dic[i][1] == maximum:
        li.append(dic[i][0])

if len(li) > 1: # 최빈값
    print(li[1])
else:
    print(li[0])
    
print(sorted(num_list)[-1] - sorted(num_list)[0]) # 범위
'''

from collections import Counter

n = int(input())

num_list = []

for i in range(n):
    num_list.append(int(input()))

print(round(sum(num_list) / n)) # 산술평균

print(sorted(num_list)[n // 2]) # 중앙값

li = Counter(sorted(num_list)).most_common()

if len(li) > 1: # 최빈값
    if li[0][1] == li[1][1]:
        print(li[1][0])
    else:
        print(li[0][0])
else:
    print(li[0][0])
    
print(sorted(num_list)[-1] - sorted(num_list)[0]) # 범위