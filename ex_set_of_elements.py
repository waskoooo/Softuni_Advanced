n , m = [int(x) for x in input().split()]

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(n)}

print(*first_set.intersection(second_set), sep="\n")

