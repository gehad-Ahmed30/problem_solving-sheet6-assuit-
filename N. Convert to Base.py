#Conversion from Base X to Decimal:Python has a built-in function int(N, X) which converts a string N from base X to a decimal integer.
def base_conversion(n,x,y):
    if n==1:
        dec_value=int(x,y)
        return dec_value
    elif n==2:
        def decimal_to_base(x,y):
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result=''
            while x>0:
                result = digits[x % y] + result
                x//=y
            return result or '0'
        base_value = decimal_to_base(int(x), y)
        return base_value

n=int(input())
x,y=input().split()
y=int(y)

print(base_conversion(n,x,y))
