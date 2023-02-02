"""
operator 함수로서의 표준 연산자
operator 모듈

operator 기능
1) 사칙 연산
operator.add(x,y) # 3 + 2
operator.sub(3,2) # 3 - 2
operator.mul(3,2) # 3 * 2
operator.truediv(3,2) # 3 / 2
operator.abs() # 절대값
operator.inv(obj)
operator.invert(obj) # 숫자(obj)의 비트별 반전을 반환
operator.countOf(a,b) # a에서 b가 발생하는 횟수
operator.getitem(a,b) # 인덱스 b에 있는 a의 값을 반환
operator.indexof(a,b) # a에서 b가 처음으로 발견되는 인덱스를 반환

2) 몫과 나머지
operator.floordiv(5,2) # 5 // 2 몫
operator.mod(5,2) # 5 % 2 나머지

3) 대 소 비교
operator.lt(3,2) # 3 < 2 ?
operator.le(3,2) # 3 <= 2 ?
operator.gt(3,2) # 3 > 2 ?
operator.ge(3,2) # 3 >= 2 ?
operator.eq(3,3) # 3 == 3 ?
operator.ne(a,b) # a != b


4) 논리 연산
operator.is_(a, 'helo') # a is 'helo'?
operator.is_not(a, 'helo') # a is not 'helo'?
operator.and_(a==3, b==2) # a == 3 and b == 2
operator.or_(a==3, b==2) # a==3 or b==2
operator.not_(obj) # not obj의 결과를 반환
operator.truth(obj) #obj가 참이면 true반환, 그렇지 않으면 false를 반환


https://docs.python.org/ko/3.7/library/operator.html 자세한 건 여기로
"""

import operator

a = [1,2,3]
b = [10,20,30]

# print(list(map(operator.add,a,b))) # map은 변환시켜 주기 list(map(int,a)) >> a에 있는 것들을 map을 통해 int로 변환 시키고 list에 집어넣어라 라는 뜻

# print(operator.lt(3,2)) # 3 < 2 ?
# print(operator.le(3,2)) # 3 < 2 ?
# print(operator.gt(3,2)) # 3 < 2 ?
# print(operator.ge(3,2)) # 3 < 2 ?
# print(operator.eq(3,2)) # 3 < 2 ?

print(operator.is_('helo', 'helo')) # a is 'helo'?
print(operator.is_not(a, 'helo')) # a is not 'helo'?
print(operator.and_(a==3, b==2)) # a == 3 and b == 2
print(operator.or_(a==3, b==2)) # a==3 or b==2