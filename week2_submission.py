# DP Approach
def f(n):
    s = [0, 1]
    for _ in range(2,n):
       s.append(s[-1] + s[-2])
    return s[0:n+1]

n = input("Input n: ")
print(f(int(n)))
