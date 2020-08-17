# 1

# def sum_n(n):
#
#     y = 0
#     for i in range(int(n)+1):
#         y = y + i
#
#     return(y)
#
# print(sum_n(10))
# print(sum_n(100))

# def 제곱 sum(n):
#
#     y = 0
#     for i in range(int(n)+1):
#         y = y + i**2
#
#     return(y)
#
# print(sum(10))
# print(sum(100))
#
#

# 2
# def maxim(list):
#
#     for element in list:
#       list.sort()
#
#     return list[-1]
#
# print(maxim([-1,3,1,-7,4,11,3,5,100]))

def max(list):

    list_1 = list
    list_2 = []

    for i in range(len(list)):
        for j in range(len(list_1)):
            if list[i] < list_1[j]:
                list_2 = list[j]
                if list_2[0] < list_1[j]:
                    list_2 = []
                    list_2 = list[j]


    print(list_2)


max([5, 456, 3, 98, 12, -3])