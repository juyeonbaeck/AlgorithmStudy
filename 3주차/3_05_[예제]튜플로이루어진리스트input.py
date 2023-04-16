#기존 값으로 튜플 입력받기
p0 = tuple(int(n0) for n0 in [1,2,3])
print(p0)

#튜플 끊어받기
p1 = tuple(int(n1) for n1 in input().split()[:2])
print(p1)

#튜플로이루어진 리스트
p2 = [tuple(int(n2) for n2 in input().split()[:2])]
print(p2)

#튜플로 이루어진 리스트 반복 --> 입력받은 리스트 중 앞에 2개 끊어서 튜플로 저장/을 세번 반복/하는 리스트
p3 = [tuple(int(n3) for n3 in input().split()[:2]) for _ in range(3)]
print(p3)

#튜플 쌍 기존값 입력받기 -> 입력값이 """이중배열""" 형태여야함!! 꼭
p4 = tuple((int(x), int(y)) for x, y in [[2,3],[3,4]])
print(p4)

#튜플 1쌍 input으로 입력받기 -> 
p5 = tuple((int(x), int(y)) for x, y in [input().split()[:2]])
print(p5)

#튜플 3쌍 input으로 입력받기
p6 = tuple((int(x), int(y)) for x, y in [input().split()[:2] for _ in range(3)])
print(p6)

#튜플로 이루어진 리스트로 만들기
p7 = [(int(x), int(y)) for x, y in [input().split()[:2] for _ in range(3)]]
print(p7)

#튜플 n쌍으로 이루어진 리스트
n = int(input())
p8 = [(int(x1), int(y1)) for x1, y1 in [input().split()[:2] for _ in range(n)]]
print(p8)