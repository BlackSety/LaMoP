import timeit
#m = [1, 8, 3, 4, 5, 9, 2, 7, 11, 1]
m=[1,2,3,4,5,6,7]
def secmin(m):
    if m[0]>m[1]: otv=m[0] , minn=m[1]
    else:
        otv=m[1]
        minn=m[0]
    for i in range(len(m)):
        if m[i] < otv and m[i] > minn:
            otv = m[i]
        if m[i] < minn:
            otv = minn
            minn = m[i]
    return(otv)
avg=0
ans=0
for i in range (5):
    otv=(timeit.repeat("secmin(m)", setup="from __main__ import secmin, m", number=10000000, repeat=5))
    avg = sum(otv)/len(otv)
    print(avg)
    ans+=avg
print(ans/5, "avg secmin")
# timeit res =  4.80250917999947
#               4.772428359999322
#               4.900338279997231
#               5.186771200000658
#               5.585673599995789
# timeit res avg = 5.049544123998495