def modify_list(mas):
    i = 0
    while i < len(mas):
        if mas[i] % 2 == 0:
            mas[i] //= 2
            i += 1
        else:
            mas.pop(i)

#    for itm in mas:
#        if itm % 2 != 0:
#            mas.remove(itm)
#    for i in range(len(mas)):
#        mas[i] //= 2


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
