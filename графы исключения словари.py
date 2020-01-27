predki, iskl = {}, []

def input_dt(x):
    predki[x[0]] = x[2:] if len(x) > 1 else []

def res(k, i):
    if k in predki.keys():
        for v in predki[k]:
            if v in iskl and iskl.index(v) < iskl.index(i) or res(v, i): return 1

for _ in range(int(input())): input_dt(input().split())
for _ in range(int(input())): iskl.append(input())

for k in iskl[1:]:
    if res(k, i = k): print(k)
