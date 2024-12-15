"""
    Реализация сортировки методом перемешивания.
"""

import datetime


a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(f"UnSorted array: {a}")

start = datetime.datetime.now()

for i in range(0, len(a)//2):
    for di in range(i, len(a)-1-i):
        if a[di] > a[di+1]:
            a[di], a[di+1] = a[di+1], a[di]
        di += 1
    for ri in range(len(a)-2-i, i, -1):
        if a[ri] < a[ri-1]:
            a[ri-1], a[ri] = a[ri], a[ri-1]
        ri -= 1
    i += 1
finish = datetime.datetime.now()

print(f"  Sorted array: {a}")

print(f"    Begin at: {str(start)}")
print(f"    End at  : {str(finish)}")
print(f"    Total time: {str(finish - start)}")
