a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# O()의 정의를 생각하면 전자의 부등식이 n >= n0에 대해 항상 성립하기 위해서는
# 계수들 간의 부등식 a1 <= c 이 필요함
print(int((a1 * n0 + a0 <= c * n0) & (a1 <= c)))

# 맞았습니다 가 뜨긴 하지만 옳은 풀이가 아님
# res = 1
# for n in range(n0, n0+100):
#     res *= int(a1 * n + a0 <= c * n)

# print(res)