"""
스택

먼저 들어간 자료가 나중에 나오는 자료구조. 유식한 말로 후입선출(後入先出) 구조라고 한다.

자료를 넣는 push 함수와 자료를 빼는 pop 함수를 갖는 게 정석이다.

empty, full 등 다른 함수들을 가질 수 있다. C++의 STL에서 지원한다.
"""

class stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

	def pop(self):
		return self.items.pop()


def reverseString(str):
    s = stack()
    result = ""
    for i in str:
        s.push(i)
    while s.isEmpty() != True:
        result += s.pop()
    return result

print(reverseString("apple"))