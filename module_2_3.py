my_list = [42, 69, 322, 13, 0, 99, -5, 9,8,7,-6, 5]
index_my_list = []
for num in my_list:
    if num >= 0: # если число положительное или 0
        index_my_list.append(num)
    else: # если есть отрицательное число
        break
print(index_my_list)