# DP Approach + Code Golf
def f(n,a=0,b=1):
    return n>0 and f(n-1,b,a+b) or (b if n else a)

n = input("Input n: ")
print(f(int(n)))
