"""
    Реализация сортировки методом пузырька.
"""

import datetime


a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(f"UnSorted array: {a}")

start = datetime.datetime.now()

for i in range(0, len(a)-1):
    for di in range(0, len(a)-1-i):
        if a[di] > a[di+1]:
            a[di], a[di+1] = a[di+1], a[di]

        di += 1

    i += 1
finish = datetime.datetime.now()

print(f"  Sorted array: {a}")

print(f"    Begin at: {str(start)}")
print(f"    End at  : {str(finish)}")
print(f"    Total time: {str(finish - start)}")

