a,b,z=map(int,input().split())
a, b = min(a, b), max(a, b)
sum_up_to_b = (b // z) * (b // z + 1) // 2 * z
sum_up_to_a_minus_1 = ((a - 1) // z) * ((a - 1) // z + 1) // 2 * z
#he formula to calculate the sum of multiples of a number z up to a limit n
result = sum_up_to_b - sum_up_to_a_minus_1

print(result)
