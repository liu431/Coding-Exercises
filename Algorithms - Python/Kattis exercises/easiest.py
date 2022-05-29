def digits_sum(n):
    k1=str(n)
    sum1=0
    for i in range(0,len(k1)):
      sum1+=int(k1[i])
    return sum1
while True:
    n=int(input())
    if n==0:
        break
    else:
        for p in range(11,10000):
            if digits_sum(n)==digits_sum(n*p):
                print(p)
                break

