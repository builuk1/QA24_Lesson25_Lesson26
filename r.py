# from mensa_logger import time_site
#
# url = 'https://www.tinkercad.com/'
# print(time_site(url))

l1 = [0, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5, 6, 7, 8]
l3 = []
len_l1 = len(l1)
len_l2 = len(l2)
f = 0
if len_l1 < len_l2:
    len_l2,len_l1 = len_l1,len_l2
    l2[:], l1[:] = l1[:], l2[:]

for i in range(len_l1):
    if i >= len_l2:
        l3.append(l1[i])
    elif i < len_l2:
        if l1[i] != l2[i]:
            l3.append(l1[i])
            l3.append(l2[i])

print(l3)