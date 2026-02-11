#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]
result = set()

for number in original:
    if number > 5:
        result.add(number + 2)

print(original)
print(result)
