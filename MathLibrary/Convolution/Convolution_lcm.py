# A: array of length INF (i >= N => A[i] = 0)
# B: array of length INF (i >= M => B[i] = 0)
# C: array of length L
# C[k] = sum(A[i]*B[j] for i, j | lcm(i, j) == k)

def primes(n):
    flg = [True]*(n+1)
    flg[0] = False
    flg[1] = False
    p = 2
    while p * p <= n:
        if flg[p]:
            for i in range(p, n//p+1):
                flg[p*i] = False
        p += 1
    res = []
    for i in range(n+1):
        if flg[i]:
            res.append(i)
    return res

def FZT(f, n):
    m = len(f)
    if m < n:
        f = f[:] + [0]*(n-m)
    p_tab = primes(n)
    res = [f[i] for i in range(n)]
    for i in p_tab:
        for j in range(1, n//i+1):
            res[i*j-1] += res[j-1]
    return res

def FMT(f, n):
    m = len(f)
    if m < n:
        f = f[:] + [0]*(n-m)
    p_tab = primes(n)
    res = [f[i] for i in range(n)]
    for i in p_tab:
        for j in range(n//i, 0, -1):
            res[i*j-1] -= res[j-1]
    return res

FA = FZT(A, L)
FB = FZT(B, L)
C = [FA[i]*FB[i] for i in range(L)]
C = FMT(C, L)
