# 문제에서는 함수만 구현하라고 하였으나 테스트를 위해 input을 받아서 출력하는 코드를 추가
# .split()을 사용하면 공백도 문자열로 인식하기 때문에 사용하지 않음
s = input()

# 제한사항 구현
# 문자열 `s`는 길이 1 이상의 영문 대소문자로만 구성됩니다.
# 따로 어떻게 예외처리를 할지 문제에서 제시하지 않았기에, 임의로 추가함
if len(s) < 1:
    raise ValueError("문자열 `s`는 길이 1 이상이어야 합니다.")
if not s.isalpha():
    raise ValueError("문자열 `s`는 영문 대소문자로만 구성되어야 합니다.")

# 첫 번째 solution. python 에서 기본적으로 제공하는 sorted() 함수를 사용
# greedy 알고리즘의 방식을 차용해 key를 ord() 함수로 설정하여 대소문자를 구분해서 정렬 후 reverse=True로 내림차순 정렬
def solution(s):
    return ''.join(sorted(s, key=lambda x: ord(x), reverse=True))

# 두 번째 solution. sorted()나 sort 함수를 사용하지 않고 직접 구현
# 단, 이 방법은 bubble sort를 사용했기에 시간복잡도가 N2가 되어 매우 비효율적
# def solution(s):
#     s = list(s)
#     n = len(s)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if ord(s[j]) < ord(s[j+1]):
#                 # 두 요소를 교환
#                 s[j], s[j+1] = s[j+1], s[j]
    
#     return ''.join(s)  # 다시 문자열로 변환하여 반환

print(solution(s))