x, y = map(int, input().split())

if x > y:
    total_sum = (x * (x + 1) // 2) - ((y - 1) * y // 2)
else:
    total_sum = (y * (y + 1) // 2) - ((x - 1) * x // 2)
print(total_sum)

start = min(x, y)
end = max(x, y)
if start % 2 != 0:
    start += 1
if end % 2 != 0:
    end -= 1
even_sum = ((end - start) // 2 + 1) * (start + end) // 2
print(even_sum)

start = min(x, y)
end = max(x, y)
if start % 2 == 0:
    start += 1
if end % 2 == 0:
    end -= 1
odd_sum = ((end - start) // 2 + 1) * (start + end) // 2
print(odd_sum)



    



