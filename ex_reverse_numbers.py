from collections import deque

#numbers = deque(input().split())

#for _ in range(len(numbers)):
#    print(numbers.pop(), end=" ")

numbers = deque(input().split())

numbers.reverse()

print(" ".join(numbers))
