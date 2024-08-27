def prime_factors(n):
    factor={}
    devisor=2
    result=[set()]
    while n>1:
        while n % devisor==0:
            if devisor in factor:
                factor[devisor] += 1
            else:
                factor[devisor] = 1
            n//=devisor
        devisor+=1   # !% 2==0
    result = []
    for prime, count in factor.items():
        result.append(f"({prime}^{count})")
   
    return('*'.join(map(str,result)))

n=int(input())
print(prime_factors(n))

