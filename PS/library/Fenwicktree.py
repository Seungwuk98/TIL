arr = [*range(1, 257)]  # 1부터 256
prefix = [0]*257

for i in range(1, 257):
    prefix[i] = prefix[i-1] + arr[i-1]

Fenwick = [0]*257

for i in range(1, 257):
    Fenwick[i] = prefix[i] - prefix[i-(i & -i)]


def update(idx, plus):
    while idx <= 256:
        Fenwick[idx] += plus
        idx += idx & -idx


def query_1_to_idx(idx):
    ret = 0
    while idx:
        ret += Fenwick[idx]
        idx -= idx & -idx
    return ret


def query_L_to_R(L, R):
    return query_1_to_idx(R) - query_1_to_idx(L-1)


print(query_L_to_R(2, 5))   # 2+3+4+5 = 14
update(3, 3)                # 3->6
print(query_L_to_R(2, 5))   # 2+6+4+5 = 17
