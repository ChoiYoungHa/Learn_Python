i = int(input())
list_a = list(map(int, input().split()))
max_num = 0
min_num = 99
for j in range(i):
    for k in range(i):
        if list_a[j] > list_a[k]:
            if max_num < list_a[j]:
                max_num = list_a[j]

        if list_a[j] < list_a[k]:
            if min_num > list_a[j]:
                min_num = list_a[j]

print(min_num, max_num)