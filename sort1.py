import random

def sort(arr):
    if len(arr) < 2:
        return
    sepI = len(arr) // 2
    L = arr[:sepI]
    R = arr[sepI:]
    sort(L)
    sort(R)
    n = 0
    m = 0
    k = 0
    buff = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            buff[k] = L[n]
            n += 1
        else:
            buff[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        buff[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        buff[k] = R[m]
        m += 1
        k += 1
    for i in range(len(arr)):
        arr[i] = buff[i]


def generateArray(l):
    arr = [0] * l
    for i in range(l):
        arr[i] = random.randint(0,100)
    return  arr


def deleteDuplicates(arr):
    sort(arr)
    i = 1
    if len(arr) < 2:
        return
    prevEl = arr[0]
    while i < len(arr):
        currEl = arr[i]
        if prevEl == currEl:
            del arr[i]
        else:
            prevEl = arr[i]
            i += 1





arr = generateArray(100)
print("изначальный массив: ",arr)
sort(arr)
print("отсортированный массив: ",arr)
deleteDuplicates(arr)
print("без дупликатов массив: ",arr)